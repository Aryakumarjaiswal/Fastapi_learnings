from fastapi import FastAPI, HTTPException,Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

)



#in main.py

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
