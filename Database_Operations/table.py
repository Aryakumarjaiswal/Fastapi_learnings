# Step 4: Defining Database Models (models.py)
# Let’s create a simple table for User.


# table.py
from sqlalchemy import Column, Integer, String
from database2 import Base

# Define the User table
class User(Base):
    __tablename__ = "users"  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    name = Column(String, index=True)  # Name column
    email = Column(String, unique=True, index=True) 
    age=Column(Integer)
     # Email column
# Explanation
# tablename: Specifies the name of the table in the database.
# Column: Used to define a column in the table.
# Integer: Data type for the column (e.g., id is an integer).
# String: Data type for the column (e.g., name and email are strings).
# primary_key=True: Marks id as the primary key.
# unique=True: Ensures that the email is unique for each user.
# index=True: Creates an index to speed up queries on these columns.
