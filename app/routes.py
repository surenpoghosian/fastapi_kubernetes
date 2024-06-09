from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Item
from app.dependencies import get_db
from app.schemas import Item as ItemSchema, ItemCreate

router = APIRouter()

@router.post("/items/", response_model=ItemSchema)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/items/{item_id}", response_model=ItemSchema)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
