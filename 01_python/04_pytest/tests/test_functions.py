# The name of the file should start with test_ and the name of the function should also start with test_
# This is how pytest knows which files and functions to run
import time
import pytest
import src.functions as functions


def test_add_numbers():
    # assertion throws an assertion error if the condition is not met
    assert functions.add(1, 2) == 3


def test_add_strings():
    assert functions.add("Hello", " World") == "Hello World"


def test_divide():
    assert functions.divide(6, 3) == 2
    assert functions.divide(5, 2) == 2.5

    # we expect a ZeroDivisionError to be raised
    with pytest.raises(ZeroDivisionError):
        functions.divide(1, 0)


# we can skip a test by using the skip decorator
@pytest.mark.skip(reason="This test is not ready yet")
def test_not_ready():
    assert functions.add(1, 2) == 3


# we can also skip a test if a condition is met
@pytest.mark.skipif(True, reason="This test is not ready yet")
def test_not_ready():
    assert functions.add(1, 2) == 3


# we can also use the xfail decorator to mark a test as expected to fail
# this is useful when we know a test is failing but we want to keep track of it
@pytest.mark.xfail
def test_expected_fail():
    assert functions.add(1, 2) == 4
