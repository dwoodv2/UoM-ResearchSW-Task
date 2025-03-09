def print_readable(fruit):
    print(f"Name:\t{fruit.name}\n"
          f"ID:\t{fruit.id}\n"
          f"Family:\t{fruit.family}\n"
          f"Sugar:\t{fruit.sugar}g\n"
          f"Carbohydrates:\t{fruit.carbohydrates}g")

def print_machine(fruit):
    print(fruit.response)