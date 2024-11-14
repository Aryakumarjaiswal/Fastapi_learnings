# main2.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from table import User, Base
from database2 import engine, SessionLocal

# Create the FastAPI app
app = FastAPI()

# Create the tables in the database
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to create a new user
@app.post("/users/")
def create_user(name: str, age: int, email: str, db: Session = Depends(get_db)):
    # Check if a user with the given email already exists
    db_user = db.query(User).filter(User.email == email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create a new user instance and add it to the database
    new_user = User(name=name, age=age, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user": new_user}

# Route to get a welcome message
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI and Database!"}
