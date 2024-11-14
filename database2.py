#Step 1:pip install fastapi sqlalchemy uvicorn


# Step 2: Create a Basic Project Structure
# Set up a simple directory structure for your FastAPI project:

# /your_project_directory
# │
# ├── main2.py
# ├── database2.py
# └── table.py

#Step 3: Setting Up Database Connectivity (database.py)
# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"#If file not there then creats automatically

# Create the SQLAlchemy engine to connect to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session factory to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our database models
Base = declarative_base()


# Explanation
# create_engine: This function creates a connection to the SQLite database. "sqlite:///./test.db" means:
# sqlite:// specifies that we are using SQLite.
# ./test.db specifies the database file path. If the file doesn’t exist, it will be created automatically.
# SessionLocal: A session is used to interact with the database (e.g., querying or inserting data).
# Base: The base class we use to define our tables.

