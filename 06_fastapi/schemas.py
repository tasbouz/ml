from enum import Enum
from pydantic import BaseModel


# Create a class that defines some predefined path parameters
class PredefinedPathParameters(str, Enum):
    value1: str = "value1"
    value2: str = "value2"
    value3: str = "value3"


# Create a class that defines the request body of
class CreateRequestBody(BaseModel):
    id: int
    name: str
    description: str

    # Add an example of a response model for the docs
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": "item1",
                    "description": "description1"
                }
            ]
        }
    }


# Create a class that defines the request body of
class ReadRequestBody(BaseModel):
    id: int

    # Add an example of a response model for the docs
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                }
            ]
        }
    }


# Create a class that defines a response model
class ResponseModel(BaseModel):
    name: str
    description: str

    # Add an example of a response model for the docs
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "item1",
                    "description": "description1"
                }
            ]
        }
    }
