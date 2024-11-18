from fastapi import FastAPI, HTTPException,Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test2.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define a sample model
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# DELETE operation using SQLAlchemy


app = FastAPI()

@app.delete("/items/{id_no}")
def delete_item(id_no: int, db: Session = Depends(get_db)):
    # Find the item by id_no
    item_to_delete = db.query(Item).filter(Item.id_no == id_no).first()

    # Check if the item exists
    if item_to_delete is None:
        raise HTTPException(status_code=404, detail="Item not found")

    # Delete the item
    db.delete(item_to_delete)
    db.commit()

    return {"message": f"Item with id_no {id_no} has been deleted successfully"}
