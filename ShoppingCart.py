class ShoppingCart:
    def __init__(self):
        self.cart = []
        self.products = [
            {"item": "Table", "price": 50.0, "dimension": "4x3 ft"},
            {"item": "Chair", "price": 20.0, "dimension": "1.5x1.5 ft"},
            {"item": "Lamp", "price": 15.0, "dimension": "2x1 ft"}
        ]

    def add_item(self, item, price):
        self.cart.append({'item': item, 'price': price})
        print(f'{item} has been added to your cart.')

    def view_cart(self):
        if not self.cart:
            return "Your cart is empty."
        else:
            cart_details = []
            for idx, item in enumerate(self.cart, start=1):
                cart_details.append(f"{idx}. {item['item']} - ${item['price']:.2f}")
            return cart_details

    def total_price(self):
        total = sum(item['price'] for item in self.cart)
        return f"Total price: ${total:.2f}"

    def get_products(self):
        return [{"item": p["item"], "price": p["price"], "dimension": p["dimension"]} for p in self.products]
