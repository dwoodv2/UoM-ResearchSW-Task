"""Provides utilites for interacting with the FruityVice API"""
import requests
from fruit_lookup_dwoodv2.utils import FruitNotFoundException
from fruit_lookup_dwoodv2.models import Fruit

API_URL = "https://www.fruityvice.com/api/fruit"

"""Gets fruit given a string as a name

    Parameters:
    argument1 (str): The string name

    Returns:
    Fruit: The fruit object if the process succeeds

"""
def get_fruit(name):
    try:
        response = requests.get(f"{API_URL}/{name}") # Send a GET request to the API to fetch fruit details by name
        if response.status_code == 404: # API returns 404 if the fruit is not found, so throw an error if this occurs.
            raise FruitNotFoundException(f"Fruit {name} not found")
        response = response.json() # Get JSON so we can parse it.
    except requests.exceptions.HTTPError as e:
        print(f"HTTP request failed for {name}")
        raise e
    # Create a fruit object from parsed JSON.
    fruit = Fruit(response["name"],response["id"],response["family"], response["nutritions"]["sugar"],
                  response["nutritions"]["carbohydrates"],response)
    return fruit
