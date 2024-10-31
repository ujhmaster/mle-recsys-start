import requests

recommendations_url = "http://127.0.0.1:8000/recommendations"
features_store_url = "http://127.0.0.1:8010/similar_items"
events_store_url = "http://127.0.0.1:8020"

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
"""params_rec = {"user_id": 1353637, 'k': 3}
params_fea = {"item_id": 17245, 'k': 3}
params_storage = {"user_id": 1291248,"item_id": 17245}
params_storage_get = {"user_id": 1127794,"k":3}
#resp = requests.post(recommendations_url, headers=headers, params=params_rec)
#resp = requests.post(features_store_url, headers=headers, params=params_fea)
#resp = requests.post(events_store_url + '/put', headers=headers, params=params_storage)
params = {"user_id": 1291248, 'k': 3}

resp = requests.post(recommendations_url + "_online", headers=headers, params=params)


if resp.status_code == 200:
    recs = resp.json()
else:
    recs = []
    print(f"status code: {resp.status_code}")
    
print(recs)
"""
user_id = 1291248
event_item_ids = [41899, 102868, 5472, 5907]

for event_item_id in event_item_ids:
    resp = requests.post(events_store_url + "/put", 
                         headers=headers, 
                         params={"user_id": user_id, "item_id": event_item_id})
                         
params = {"user_id": user_id, 'k': 5}

resp = requests.post(recommendations_url + "_online", headers=headers, params=params)
online_recs = resp.json()
    
print(online_recs) 