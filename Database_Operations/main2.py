# main2.py

from fastapi import FastAPI, Depends, HTTPException,status
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


# Why We Write db: Session = Depends(get_db)
# db: This is like the library card you need to interact with the books (database).
# Session: Just as a library card gives you access to borrow books, Session gives you access to the database.
# Depends(get_db): This is like the helpful librarian who automatically gives you the card when you need it and takes it back when you're done.
# get_db is a function that creates and returns a database connection.



# Route to create a new user
@app.post("/users/",status_code=201) # or @app.post("/users/",status_code=status.create)
def create_user(name: str, age: int, email: str, db: Session = Depends(get_db)):
    # Check if a user with the given email already exists
    db_user = db.query(User).filter(User.email == email).first()#WHERE<-Filter
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
def read_root(db: Session = Depends(get_db)):
    query_response=db.query(User).all()

    return {"message": "Hello, FastAPI and Database!",
            "See the Table":query_response}



#In swagger UI for successful execution  for any operation we see status code 200.There should be 
# some differentiating factor.Here its done defining status_code in path parameter.Explore HTTP Status code documentation

