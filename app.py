from fastapi import FastAPI
from typing import List, Dict
from contextlib import asynccontextmanager

cheaters = set()
fair_players = set()

def get_saved_elements(filename):
    read_set = set()
    with open(filename, 'r') as file:
        for line in file:
            item = line.strip()
            read_set.add(item)
    return read_set

def save_elements(filename, set):
    with open(filename, 'w') as file:
        for item in set:
            file.write(item + '\n')

@asynccontextmanager
async def lifespan(app: FastAPI):
    cheaters.update(get_saved_elements("cheaters.txt"))
    fair_players.update(get_saved_elements("fair_players.txt"))
    yield

app = FastAPI(lifespan=lifespan)
requests = {
    "cheaters_count": 0,
    "fair_players_count" :0
}

@app.post("/add_cheaters/")
def add_item(items: List[str]):
    for item in items:
        cheaters.add(item)
    requests["cheaters_count"] += 1
    if requests["cheaters_count"] % 10000 == 0:
        requests["cheaters_count"] += 1
        save_elements("cheaters.txt", cheaters)
    return {"statusCode": 200}

@app.post("/add_fair_players/")
def add_item(items: List[str]):
    for item in items:
        fair_players.add(item)
    requests["fair_players_count"] += 1
    if requests["fair_players_count"] % 10000 == 0:
        requests["fair_players_count"] += 1
        save_elements("fair_players.txt", fair_players)
    return {"statusCode": 200}

@app.post("/query_items/")
def query_items(items: List[str]):
    cheaters_list = []
    fair_players_list = []
    for item in items:
        if item in cheaters:
            cheaters_list.append(item)
        elif item in fair_players:
            fair_players_list.append(item)
    return {
        "body": {
            "cheaters_list": cheaters_list,
            "fair_players_list": fair_players_list
        },
        "statusCode": 200
    }


@app.put("/clear_cache/")
def clear_cache():
    cheaters.clear()
    fair_players.clear()
    requests["cheaters_count"] = 0
    requests["fair_players_count"] = 0
    return {"statusCode": 200}
