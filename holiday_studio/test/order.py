import json
import requests

base_url = "http://127.0.0.1:5000/order"

post_data = {"price": 279287,
             "title": "ORDER%^^",
             "describtion": "HGJGJVHGCGFXDTRDYGVJH"}

post_order_response = requests.post(base_url, json=post_data)
order_id = post_order_response.json()["id"]

post_data = {"price": 279,
             "title": "ORDERyguyU",
             "describtion": "IUFHEURHIRUHWIU"}

post_order_response = requests.post(base_url, json=post_data)
order_id2 = post_order_response.json()["id"]