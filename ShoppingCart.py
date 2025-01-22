class ShoppingCart:
    def __init__(self):
        self.cart = []

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