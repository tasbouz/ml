# In this file we can define fixtures that can be used in multiple test files
import pytest


@pytest.fixture
def some_numbers_created_in_conftest():
    return 3, 4
