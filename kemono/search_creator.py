import json


import requests


from . import read_from_cache


def __fetch_creators(cache_file: str) -> str:
    response = requests.get("https://kemono.su/api/v1/creators.txt")
    data = response.text
    with open(cache_file, "w+") as creators:
        creators.write(data)
    creators.close()
    return data

def get_creators() -> list[str]:
    return json.loads(read_from_cache(__fetch_creators, fname="creators.txt", delay=1))

def get_creator(name: str) -> dict | None:
    for creator in get_creators():
        if name.lower() == creator["name"].lower():
            return creator
    return None
