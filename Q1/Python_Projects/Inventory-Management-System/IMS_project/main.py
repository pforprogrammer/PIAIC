from typing import Optional, Dict

class User:
    def __init__(self, username: str, password: str, role: str) -> None:
        self.username: str = username
        self.password: str = password
        self.role: str = role

    def authenticate(self, password: str) -> bool:
        return self.password == password


class Product:
    def __init__(self, product_id: str, name: str, category: str, price: float, stock_quantity: int) -> None:
        self.product_id: str = product_id
        self.name: str = name
        self.category: str = category
        self.price: float = price
        self.stock_quantity: int = stock_quantity

    def update_stock(self, quantity: int) -> None:
        self.stock_quantity += quantity

    def display_details(self) -> None:
        print(f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, "
              f"Price: {self.price}, Stock: {self.stock_quantity}")


class InventoryManagementSystem:
    MINIMUM_STOCK_THRESHOLD: int = 10

    def __init__(self) -> None:
        self.users: Dict[str, User] = {}  # Dictionary to store users
        self.products: Dict[str, Product] = {}  # Dictionary to store products
        self.current_user: Optional[User] = None

    def add_user(self, username: str, password: str, role: str) -> None:
        self.users[username] = User(username, password, role)

    def login(self) -> bool:
        username = input("Username: ")
        password = input("Password: ")
        user = self.users.get(username)
        if user and user.authenticate(password):
            self.current_user = user
            print(f"Welcome, {self.current_user.username}!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def add_product(self) -> None:
        if self.current_user.role != "Admin":
            print("Permission denied. Only Admin can add products.")
            return

        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        price = float(input("Enter Price: "))
        stock_quantity = int(input("Enter Stock Quantity: "))
        if product_id in self.products:
            print("Product with this ID already exists.")
            return
        self.products[product_id] = Product(product_id, name, category, price, stock_quantity)
        print("Product added successfully.")

    def view_products(self) -> None:
        if not self.products:
            print("No products available.")
            return
        for product in self.products.values():
            product.display_details()
            if product.stock_quantity < self.MINIMUM_STOCK_THRESHOLD:
                print(" - Low stock! Consider restocking.")

    def search_product(self) -> None:
        name = input("Enter Product Name (leave blank to skip): ")
        category = input("Enter Category (leave blank to skip): ")
        results = [product for product in self.products.values()
                   if (name and product.name == name) or (category and product.category == category)]
        if not results:
            print("No matching products found.")
        else:
            for product in results:
                product.display_details()

    def edit_product(self) -> None:
        if self.current_user.role != "Admin":
            print("Permission denied. Only Admin can edit products.")
            return
        product_id = input("Enter Product ID to edit: ")
        product = self.products.get(product_id)
        if not product:
            print("Product not found.")
            return

        name = input("New Name (leave blank to skip): ")
        category = input("New Category (leave blank to skip): ")
        price = input("New Price (leave blank to skip): ")
        stock_quantity = input("New Stock Quantity (leave blank to skip): ")
        if name:
            product.name = name
        if category:
            product.category = category
        if price:
            product.price = float(price)
        if stock_quantity:
            product.stock_quantity = int(stock_quantity)
        print("Product updated successfully.")

    def delete_product(self) -> None:
        if self.current_user.role != "Admin":
            print("Permission denied. Only Admin can delete products.")
            return
        product_id = input("Enter Product ID to delete: ")
        if product_id in self.products:
            del self.products[product_id]
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def logout(self) -> None:
        self.current_user = None
        print("Logged out.")

    def run(self) -> None:
        self.add_user("admin", "adminpass", "Admin")
        self.add_user("user", "userpass", "User")

        while True:
            if not self.current_user:
                if not self.login():
                    continue

            if self.current_user.role == "Admin":
                print("\nAdmin Menu: 1. Add Product, 2. Edit Product, 3. Delete Product, 4. View Products, 5. Search Product, 6. Logout")
            else:
                print("\nUser Menu: 1. View Products, 2. Search Product, 3. Logout")

            choice = input("Choose an option: ")

            if self.current_user.role == "Admin":
                if choice == "1":
                    self.add_product()
                elif choice == "2":
                    self.edit_product()
                elif choice == "3":
                    self.delete_product()
                elif choice == "4":
                    self.view_products()
                elif choice == "5":
                    self.search_product()
                elif choice == "6":
                    self.logout()
            else:
                if choice == "1":
                    self.view_products()
                elif choice == "2":
                    self.search_product()
                elif choice == "3":
                    self.logout()


if __name__ == "__main__":
    ims = InventoryManagementSystem()
    ims.run()
