# The name of the file should start with test_ and the name of the function should also start with test_
# This is how pytest knows which files and functions to run
import math
import pytest
from src.classes import Circle
from tests.conftest import circle_created_in_conftest


# FIRST WAY: TEST WITH CLASS
class TestCircle:

    # special function that runs before each test method (needs to run pytest with -s flag to see the print statements)
    def setup_method(self, method):
        print(f"Setting up {method}")
        # create a new instance of Circle available to each test method
        self.circle = Circle(radius=5)

    # special function that runs after each test method (needs to run pytest with -s flag to see the print statements)
    def teardown_method(self, method):
        print(f"Tearing down {method}")
        # delete the instance of Circle after each test method
        del self.circle

    def test_area(self, circle_created_in_conftest):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
        # we can also use the fixture created in conftest.py
        assert circle_created_in_conftest.area() == math.pi * circle_created_in_conftest.radius ** 2

    def test_perimeter(self, circle_created_in_conftest):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius
        assert circle_created_in_conftest.perimeter() == 2 * math.pi * circle_created_in_conftest.radius


# SECOND WAY: TEST WITH FUNCTIONS

# With classes we can create an object to be shared among the test methods using the setup_method
# With functions we can do the same using fixtures
@pytest.fixture
def circle_created_in_test_file():
    return Circle(radius=5)


def test_area(circle_created_in_test_file, circle_created_in_conftest):
    assert circle_created_in_test_file.area() == math.pi * circle_created_in_test_file.radius ** 2
    # we can also use the fixture created in conftest.py
    assert circle_created_in_conftest.area() == math.pi * circle_created_in_conftest.radius ** 2


def test_perimeter(circle_created_in_test_file, circle_created_in_conftest):
    assert circle_created_in_test_file.perimeter() == 2 * math.pi * circle_created_in_test_file.radius
    assert circle_created_in_conftest.perimeter() == 2 * math.pi * circle_created_in_conftest.radius
