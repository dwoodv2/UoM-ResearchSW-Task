"""Represents a fruit object"""
class Fruit:
    def __init__(self, name, id, family, sugar, carbohydrates, response):
        self.name = name
        self.id = id
        self.family = family
        self.sugar = sugar
        self.carbohydrates = carbohydrates
        self.response = response  # The JSON response
