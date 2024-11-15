from fastapi import APIRouter

# Create an instance of APIRouter
router = APIRouter()

# Route 1: Get all items
@router.get("/item")
def get_items():
    return {"message": "Here are your items!"}

# Route 2: Get a specific item by ID
@router.get("/item/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "message": "Here is your item!"}

# Route 3: Create a new item
@router.post("/item")
def create_item(item: dict):
    return {"message": "Item created!", "item": item}
