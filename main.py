from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from ShoppingCart import ShoppingCart

# FastAPI app
app = FastAPI()
cart = ShoppingCart()

# Define Item first, so it can be used in PurchaseOrder
class Item(BaseModel):
    item: str
    price: float

class PurchaseOrder(BaseModel):
    items: List[Item]

@app.get("/view_items")
def view_items():
    items = cart.get_products()
    return {"products": items}

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

@app.post("/purchase_order")
def purchase_order(order: PurchaseOrder):
    for item in order.items:
        cart.add_item(item.item, item.price)
    return {"message": "Your purchase order has been placed."}
