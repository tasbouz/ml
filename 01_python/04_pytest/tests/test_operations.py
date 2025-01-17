# The name of the test file should start with test_ so pytest can automatically find it
# A good practice is to name the test file the same as the file we are testing: test_{file_name}.py
import pytest
from src.operations import add, multiply


##########
# BASICS #
##########

# The name of the testing function should also start with test_ so pytest can automatically find it
def test_add_numbers():
    # Assertion throws an assertion error if the condition is not met
    assert add(1, 2) == 3


def test_add_strings():
    assert add("Hello", " World") == "Hello World"


# Multiple assertions in one function is possible but not recommended since it makes it hard to realize what is failing
def test_multiple_adds_non_reccomended_way():
    assert add(1, 2) == 3
    assert add("Hello", " World") == "Hello World"


##########
# MARKS  #
##########

# Reccomended way is to either write one assertion per function or combine multiple assertions in one function with the
# parametrize decorator which takes the name of the variables and a list of tuples with the values to test
@pytest.mark.parametrize("n1, n2, expected", [(1, 2, 3), ("Hello", " World", "Hello World")])
def test_multiple_adds_recommended_way(n1, n2, expected):
    assert add(n1, n2) == expected


# On top of the parametrize decorator, @pytest.mark offers also other decorators used to alter the behavior of tests
# Skip a test by using the skip decorator
@pytest.mark.skip(reason="This test is not ready yet")
def test_not_ready():
    assert add(1, 2) == 3


# Skip a test conditionaly by using the skipif decorator
@pytest.mark.skipif(True, reason="This test is not ready yet")
def test_not_ready_conditional():
    assert add(1, 2) == 3


# Mark a test as expected to fail by using the xfail decorator (useful for tests that are not ready yet)
@pytest.mark.xfail
def test_expected_fail():
    assert add(1, 2) == 4


############
# FIXTURES #
############

# Similarly we can test for other functions
def test_multiply_numbers():
    assert multiply(1, 2) == 2


# Notice that we used the same numbers (1, 2) in both add and multiply tests. Instead of repeating the numbers in each
# test, we can create a fixture decorator that returns the numbers. That way the numbers can be shared among the tests
@pytest.fixture
def some_numbers():
    return 1, 2


# The fixture is then passed as an argument to the test function
def test_add_numbers_with_fixture(some_numbers):
    assert add(some_numbers[0], some_numbers[1]) == 3


def test_multiply_numbers_with_fixture(some_numbers, some_numbers_created_in_conftest):
    assert multiply(some_numbers[0], some_numbers[1]) == 2
    # We can also use the fixtures created in conftest.py
    assert multiply(some_numbers_created_in_conftest[0], some_numbers_created_in_conftest[1]) == 12


##################################
# OPTIONAL: TEST THROUGH CLASSES #
##################################

# We can also use classes to group tests together
# The name of the class function should also start with Test so pytest can automatically find it
class TestOperations:

    # Special function that runs before each test method (needs to run pytest with -s flag to see the print statements)
    def setup_method(self, method):
        print(f"Setting up {method}")
        # We can define the numbers to be shared among the test methods in the class here, instead of using fixtures
        self.n1 = 1
        self.n2 = 2

    # Special function that runs after each test method (needs to run pytest with -s flag to see the print statements)
    def teardown_method(self, method):
        print(f"Tearing down {method}")
        # Delete the instance of Circle after each test method
        del self.n1
        del self.n2

    # The name of the test methods should also start with test_ so pytest can automatically find them
    @pytest.mark.parametrize("n1, n2, expected", [(1, 2, 3), (3, 4, 7)])
    def test_add_numbers(self, n1, n2, expected):
        assert add(n1, n2) == expected

    def test_multiply_numbers(self, some_numbers_created_in_conftest):
        assert multiply(self.n1, self.n2) == 2
        assert multiply(some_numbers_created_in_conftest[0], some_numbers_created_in_conftest[1]) == 12
