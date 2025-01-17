# Mocking is a way to test interactions between the code and external dependencies, without actually calling the
# external dependencies. This is useful when one does not know what the response of the external dependency will be, or
# when one wants to test the code in isolation so she avoids side effects from services that she is not responsible for.
import requests
import pytest
import src.service as service
import unittest.mock as mock


# Mocking a connection to a fake database
@mock.patch("src.service.get_user_data")
def test_get_user_data(mock_get_user_data):
    # Mocking the response of the get_user_data function to some predefined, fake data
    mock_get_user_data.return_value = {"name": "Mocked John", "surname": "Mocked Doe"}
    # Calling the actual function, but it will now return the mocked data instead of the real data defined in service.py
    user_name = service.get_user_data("user1")

    assert user_name == {"name": "Mocked John", "surname": "Mocked Doe"}


# Mocking a succesful connection to an external API
@mock.patch("requests.get")
def test_get_users(mock_get_users):
    # Mocking the status code and the json response of the get request to a successful response
    mock_get_users.return_value.status_code = 200
    mock_get_users.return_value.json.return_value = [{"name": "John", "surname": "Doe"}]

    users = service.get_users()

    assert users == [{"name": "John", "surname": "Doe"}]


# Mocking a failed connection to an external API
@mock.patch("requests.get")
def test_get_users_error(mock_get_users):
    # Mocking the status code of the get request to a failed response
    mock_get_users.return_value.status_code = 400

    with pytest.raises(requests.HTTPError):
        service.get_users()
