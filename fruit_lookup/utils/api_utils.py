import requests
from utils.FruitNotFoundException import FruitNotFoundException
from models.fruit import Fruit

API_URL = "https://www.fruityvice.com/api/fruit"

def get_fruit(name):
    try:
        response = requests.get(f"{API_URL}/{name}")
        if response.status_code == 404:
            raise FruitNotFoundException(f"Fruit {name} not found")
        response = response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP request failed for {name}")
        raise e
    fruit = Fruit(response["name"],response["id"],response["family"], response["nutritions"]["sugar"],
                  response["nutritions"]["carbohydrates"],response)
    return fruit

