# Create a folder for your project and add the following files:
# main3.py: The main file where your FastAPI app will be.
# routes/: A folder to organize your routes.
# init.py: (An empty file to make the folder a Python package.)
# item.py: A file where you will define your routes using APIRouter().


from fastapi import FastAPI
from routes import item # Import the routes you will create

app = FastAPI()

# Include the routes from the items file
app.include_router(item.router)

# Run the server using: uvicorn main:app --reload











# Summary
# Without APIRouter(): All routes are in one main file, making the code difficult to maintain and scale.
# With APIRouter(): Routes are modular, making the code clean, organized, and scalable.
# This organization is especially useful for large projects with many endpoints, as it helps separate logic and improve maintainability.

