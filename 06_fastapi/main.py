# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python
# FastAPI doesn't have a built-in development server, so an Asynchronous Server Gateway Interface (ASGI) is required
# Here we use Uvicorno. To launch the FastAPI app, run: uvicorn main:app --reload. The server starts on localhost:8000
# FastAPI automatically generates a Swagger UI for the API. To access the Swagger UI, go to localhost:8000/docs
# FastAPI also generates a ReDoc UI for the API. To access the ReDoc UI, go to localhost:8000/redoc
# FastAPI generates an API schema using the OpenAPI standard. To access the schema, go to localhost:8000/openapi.json
import time
from fastapi import FastAPI, status, HTTPException, BackgroundTasks
from schemas import PredefinedPathParameters, CreateRequestBody, ReadRequestBody, ResponseModel

# Define tags_metadata to add metadata in the categories of the paths in the documentation
tags_metadata = [
    {
        "name": "home",
        "description": "Operations related to the root page",
        "externalDocs": {
            "description": "FastAPI Documentation",
            "url": "https://fastapi.tiangolo.com/"
        }
    },
    {
        "name": "path_parameters",
        "description": "Operations related to path parameters",
        "externalDocs": {
            "description": "Path parameters",
            "url": "https://fastapi.tiangolo.com/tutorial/path-params/"
        }
    },
    {
        "name": "query_parameters",
        "description": "Operations related to query parameters",
        "externalDocs": {
            "description": "Query parameters",
            "url": "https://fastapi.tiangolo.com/tutorial/query-params/"
        }
    },
    {
        "name": "db",
        "description": "Operations related to the database",
    },
    {
        "name": "background_task",
        "description": "Operations related to background tasks",
        "externalDocs": {
            "description": "Background tasks",
            "url": "https://fastapi.tiangolo.com/tutorial/background-tasks/"
        }
    }
]

# Create an instance of FastAPI class and define the title, description, and version of the API for the documentation
app = FastAPI(
    title="FastAPI Demo",
    description="A simple FastAPI demo. For any questions, please contact @johndoe",
    version="1.0.0",
    openapi_tags=tags_metadata)


# Define a path (or endpoint, or route) for a GET operation for the root page
@app.get("/", tags=["home"])  # Define the path and a tag for categorizing the path in the documentation
async def root() -> dict:  # Define the function that will be executed when the path is accessed
    return {"message": "Hello World"}


# Define a path for a GET HTTP method (or operation) that explains the "/path_parameters" path defined right next
# ORDER MATTERS: It is important to define this path BEFORE the path that uses the path parameter otherwise FastAPI will
# interpret the "/about" as a path parameter instead of a path and will not be able to access the path
@app.get("/path_parameters/about" , tags=["path_parameters"])
async def about_path_parameters() -> dict:
    return {"message": "This route is used to demonstrate how to access path parameters in FastAPI"}


# Define a path for a GET operation that can access a path parameter (e.g: /path_parameters/5)
@app.get("/path_parameters/{p}", tags=["path_parameters"])
async def read_path_parameters(p: int) -> dict:  # Declaring the type of the parameter will validate the input
    return {"path_parameter": p}


# Define a path for a GET operation that can access specific, predefined, path parameters
@app.get("/predefined_path_parameters/{p}", tags=["path_parameters"])
async def read_predefined_path_parameters(p: PredefinedPathParameters) -> dict:
    if p == PredefinedPathParameters.value1:
        return {"parameter": p, "message": "This is the first predefined value"}
    elif p == PredefinedPathParameters.value2:
        return {"parameter": p, "message": "This is the second predefined value"}
    else:
        return {"parameter": p, "message": "This is the third predefined value"}


# Define a path for a GET operation that can access query parameters (e.g: /query_parameter?q1=5&q2=10)
@app.get("/query_parameters", tags=["query_parameters"])
async def read_query_parameters(q1: int, q2: int = 5) -> dict:
    return {"sum": q1 + q2}

# Create a fake database to simulate a database
fake_db = {}


# Create a path for a POST operation that creates an item in the database
@app.post("/db/create", status_code=status.HTTP_201_CREATED,  tags=["db"])  # Define the status code for the response
async def create_db(request_body: CreateRequestBody) -> CreateRequestBody:  # Declare request body's type from schemas
    fake_db[request_body.id] = request_body  # Add the item to the fake database
    return request_body  # Return the request body as the response


# Create a path for a POST operation that reads an item from the fake database
@app.post("/db/read", response_model=ResponseModel, tags=["db"])  # Define the response model for the response
async def read_db(request_body: ReadRequestBody) -> CreateRequestBody:
    if request_body.id not in fake_db:  # Raise an exception if the item is not in the fake database
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return fake_db[request_body.id]  # This will be fed into the response model and returned as the response


# Create a fake background task that sleeps for 5 seconds (to simulate a long-running task)
def fake_background_task():
    time.sleep(5)
    print("Fake background task completed")


# Create a path for a POST operation that runs a background task
@app.post("/background_task", tags=["background_task"])
async def run_background_task(background_tasks: BackgroundTasks) -> dict:
    background_tasks.add_task(fake_background_task)
    return {"message": "Background task started"}
