from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()
cheaters = set()
fair_players = set()

@app.post("/add_cheaters/")
def add_item(items: List[str]):
    for item in items:
        cheaters.add(item)
    return {"statusCode": 200}

@app.post("/add_fair_players/")
def add_item(items: List[str]):
    for item in items:
        fair_players.add(item)
    return {"statusCode": 200}

@app.post("/query_items/")
def query_items(items: List[str]):
    cheaters_list = []
    for item in items:
        if item in cheaters:
            cheaters_list.append(item)
    return {
        "body": cheaters_list,
        "statusCode": 200
    }
