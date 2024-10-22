import logging

from fastapi import FastAPI
from contextlib import asynccontextmanager
from .recsys_hendler import Recommendations

rec_store = Recommendations()
logger = logging.getLogger("uvicorn.error")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # код ниже (до yield) выполнится только один раз при запуске сервиса
    logger.info("Starting")
    rec_store.load(
        "personal",
        path="./goodsread/final_recommendations_feat.parquet",
        columns=["user_id", "item_id", "rank"],
    )
    rec_store.load(
        "default",
        path="./goodsread/candidates/top_recs.parquet",
        columns=["item_id", "rank"],
    )
    yield
    # этот код выполнится только один раз при остановке сервиса
    rec_store.stats()
    logger.info("Stopping")
    
# создаём приложение FastAPI
app = FastAPI(title="recommendations", lifespan=lifespan)

@app.post("/recommendations")
async def recommendations(user_id: int, k: int = 100):
    """
    Возвращает список рекомендаций длиной k для пользователя user_id
    """

    recs = rec_store.get(user_id=user_id, k=k)

    return {"recs": recs}