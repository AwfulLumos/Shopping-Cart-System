from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from ShoppingCart import ShoppingCart

# FastAPI app
app = FastAPI()
cart = ShoppingCart()

class Item(BaseModel):
    item: str
    price: float

@app.post("/add_item")
def add_item(item: Item):
    cart.add_item(item.item, item.price)
    return {"message": f"{item.item} has been added to your cart."}

@app.get("/view_cart")
def view_cart():
    cart_contents = cart.view_cart()
    return {"cart": cart_contents}

@app.get("/total_price")
def total_price():
    total = cart.total_price()
    return {"total_price": total}