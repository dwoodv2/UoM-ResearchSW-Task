# UoM-ResearchSW-Task
Provides utilities for interacting with the [FruityVice API](https://www.fruityvice.com/).
## Usage

### As a package

To run this code as a package, you can build and install it (via pip) as follows:

```bash
pip install build  # If build not installed
python -m build
pip install dist/fruit_lookup_dwoodv2-0.0.1.tar.gz
```

Then to peform functions such as printing you can import this package and run it as follows:

```python
$ python
>>> from fruit_lookup_dwoodv2.utils import *
>>> apple = get_fruit("apple") # Get the fruit from the API
>>> print_readable(apple) # Print readable representation
Name:	Apple
ID:	6
Family:	Rosaceae
Sugar:	10.3g
Carbohydrates:	11.4g
>>> print_machine(apple) # Get machine readable (JSON)
{'name': 'Apple', 'id': 6, 'family': 'Rosaceae', 'order': 'Rosales', 'genus': 'Malus', 'nutritions': {'calories': 52, 'fat': 0.4, 'sugar': 10.3, 'carbohydrates': 11.4, 'protein': 0.3}}
```

### Using main.py

You can run the program using `main.py` which just prompts infinitely for the name of the fruit

```bash
python3 fruit_lookup_dwoodv2/main.py
```

## Testing

To run the test suite, you need to [install Pytest](https://docs.pytest.org/en/stable/getting-started.html#get-started), you can install and run the suite as follows:

```bash
cd fruit_lookup_dwoodv2/tests # Go to test directory
pytest -v
```
