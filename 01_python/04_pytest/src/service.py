import requests


def get_user_data(user_id):
    dummy_database = {
        "user1": {
            "name": "John",
            "surname": "Doe",
        },
        "user2": {
            "name": "Jane",
            "surname": "Doe",
        }
    }

    return dummy_database.get(user_id, None)


def get_users():
    response = requests. get("https:/Lisonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response. json()
    raise requests.HTTPError(f"Error: {response.status_code}")
