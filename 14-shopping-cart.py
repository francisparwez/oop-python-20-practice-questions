# 14. Shopping Cart 🛒
# Create:
#     Product
#     ShoppingCart
# Product should contain:
#     name
#     price
#     quantity
# ShoppingCart should allow:
#     add_product()
#     remove_product()
#     calculate_total()
#     display_cart()
# Example:
#     Laptop × 1 = 100000
#     Mouse × 2 = 3000
#     Total = 103000

class Product:    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def total_price(self):
        return self.price * self.quantity

class ShoppingCart:    
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        
        for p in self.products:
            if p.name.lower() == product.name.lower():
                p.quantity += product.quantity
                return
        self.products.append(product)
                
    def remove_product(self, product_name: str):
        for p in self.products:
            if p.name.lower() == product_name.lower():
                self.products.remove(p)
                print(f"🛒 Removed {product_name} from the cart.")
                return
        print(f"❌ {product_name} not found in the cart.")

    def calculate_total(self) -> float:
        return sum(product.total_price() for product in self.products)

    def display_cart(self):
        if not self.products:
            print("🛒 Your shopping cart is empty.")
            return
        
        print("\n--- Shopping Cart ---")
        for p in self.products:
            print(f"{p.name} × {p.quantity} = {p.total_price():.0f}")
        print(f"Total = {self.calculate_total():.0f}")
        print("---------------------\n")


# --- Example Usage ---
if __name__ == "__main__":
    cart = ShoppingCart()

    prod1 = Product("Laptop", 100000, 1)
    prod2 = Product("Mouse", 1500, 2)

    cart.add_product(prod1)
    cart.add_product(prod2)

    cart.display_cart()

    cart.remove_product("Mouse")
    cart.display_cart()