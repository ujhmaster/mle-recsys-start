from recsys_hendler import Recommendations

rec_store = Recommendations()

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

print(rec_store.get(user_id=1049126, k=5))
