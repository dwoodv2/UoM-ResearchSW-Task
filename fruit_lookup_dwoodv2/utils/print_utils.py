"""Provides utilities for printing Fruit objects."""
"""Prints a fruit in a human readable way.

    Parameters:
    argument1 (Fruit): A fruit object

"""
def print_readable(fruit):
    print(f"Name:\t{fruit.name}\n"
          f"ID:\t{fruit.id}\n"
          f"Family:\t{fruit.family}\n"
          f"Sugar:\t{fruit.sugar}g\n"
          f"Carbohydrates:\t{fruit.carbohydrates}g")

"""Prints a fruit in a machine readable way (JSON)

    Parameters:
    argument1 (Fruit): A fruit object

"""
def print_machine(fruit):
    print(fruit.response)
