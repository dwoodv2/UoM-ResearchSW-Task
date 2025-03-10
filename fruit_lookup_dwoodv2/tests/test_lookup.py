import pytest
from fruit_lookup_dwoodv2.models.fruit import Fruit
from fruit_lookup_dwoodv2.utils import FruitNotFoundException
from fruit_lookup_dwoodv2.utils import print_readable
class TestLookup:

    @pytest.fixture
    def setup(self):
        print("Running tests...")

    @pytest.mark.parametrize(
        "name",
        [
            "Banana", "Apple", "pEar","STRAWBERRY"
        ],
    )
    def test_get_fruit_valid(self, name):
        from fruit_lookup_dwoodv2.utils import get_fruit
        assert get_fruit(name).__class__== Fruit # Test if the result is a fruit

    @pytest.mark.parametrize(
        "name",
        [
            "Wineberry", "Appple"
        ],
    )

    def test_get_fruit_invalid(self, name):
        from fruit_lookup_dwoodv2.utils import get_fruit
        with pytest.raises(FruitNotFoundException):
            get_fruit(name) # Should throw FruitNotFoundException

    @pytest.mark.parametrize(
        "name, stdout",
        [
            ("Banana","Name:\tBanana\nID:\t1\nFamily:\tMusaceae\nSugar:\t17.2g\nCarbohydrates:\t22.0g\n"),
        ],
    )

    def test_print_fruit_valid(self, name, stdout):
        from fruit_lookup_dwoodv2.utils import get_fruit
        from fruit_lookup_dwoodv2.utils import print_readable
        import sys
        from io import StringIO
        fruit = get_fruit(name)
        temp_out = StringIO() # Redirect stdout
        sys.stdout = temp_out
        print_readable(fruit)
        assert temp_out.getvalue() == stdout
