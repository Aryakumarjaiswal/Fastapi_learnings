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


## 1. What is a "thread"?
# A thread is a separate sequence of instructions that a program can run. You can think of a thread like a person doing a specific task.
# Multiple threads mean multiple "people" working on different tasks simultaneously within a program.
# In the context of your database, multiple threads could mean that different parts of your application are trying to access or change the database at the same time.
# For example, if your web application handles many users, each user interaction may be handled by a different thread.
### Why do we use check_same_thread=False? 
By default, SQLite requires that the same thread that creates a database connection should be the only one to use it. However,
# when building a web application, we may need to let different parts (threads)
# of the app use the same database connection. Setting check_same_thread=False allows this.





# Create a session factory to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 2. What does "flushing" mean in this context?
# Flushing in SQLAlchemy means pushing the changes you made in your Python code to the database so that they are ready to be saved.
# When you work with the database using a session, you make changes (like adding or updating data) in a temporary way. These changes are kept in memory and not immediately sent to the database.
# Normally, SQLAlchemy might automatically flush these changes when needed, like before running a query. By setting autoflush=False, you turn off this automatic behavior.
# Explicit flushing: You can choose to manually synchronize (flush) your changes to the database whenever you want by calling session.flush(). This is useful if you want more control over when the
# changes are pushed but not yet permanently saved. Note that session.commit() will flush changes and then save them permanently.


# Base class for our database models
Base = declarative_base()


# Explanation
# create_engine: This function creates a connection to the SQLite database. "sqlite:///./test.db" means:
# sqlite:// specifies that we are using SQLite.
# ./test.db specifies the database file path. If the file doesn’t exist, it will be created automatically.
# SessionLocal: A session is used to interact with the database (e.g., querying or inserting data).
# Base: The base class we use to define our tables.

