# In this file we can define fixtures that can be used in multiple test files
import pytest

from src.classes import Circle


@pytest.fixture
def circle_created_in_conftest():
    return Circle(radius=5)
