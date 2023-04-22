import os
import requests

API_URL = "https://api-inference.huggingface.co/models/felakoum/distilbert-base-uncased-analysis"
headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
