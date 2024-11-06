# Inventory Management System

An interactive console-based Inventory Management System written in Python. It allows users with different roles (Admin and User) to manage and view products within the inventory. This system supports features like user authentication, adding, editing, deleting, and viewing products, as well as searching products by name or category.

## Features

### User Roles
- **Admin:** Has full access to add, edit, delete, view, and search products.
- **User:** Has limited access; can only view and search products.

### Functionalities
1. **User Authentication**: Login system to verify user credentials.
2. **Product Management (Admin only)**:
   - Add a new product with unique ID, name, category, price, and stock quantity.
   - Edit an existing product's details, including name, category, price, and stock quantity.
   - Delete a product by its ID.
3. **Product Viewing**:
   - View all products, including details like product ID, name, category, price, and stock quantity.
   - Alert for low-stock products when stock quantity falls below a threshold.
4. **Product Search**:
   - Search products by name and category.
5. **Session Management**: Logout feature to end the current user session.

### Data Storage
The system uses in-memory data storage (dictionaries) to keep track of:
- **Users**: Stored as a dictionary with usernames as keys.
- **Products**: Stored as a dictionary with product IDs as keys.

### Constants
- `MINIMUM_STOCK_THRESHOLD`: A predefined threshold (default set to 10) that triggers a low-stock warning when viewing products.

## Project Structure

The project is organized into three main classes:

1. **User**: Handles user properties and authentication.
   - **Attributes**:
     - `username` (str): Username of the user.
     - `password` (str): Password of the user.
     - `role` (str): Role of the user (Admin or User).
   - **Methods**:
     - `authenticate(password: str) -> bool`: Verifies if the input password matches the stored password.

2. **Product**: Manages product information and stock updates.
   - **Attributes**:
     - `product_id` (str): Unique identifier for the product.
     - `name` (str): Name of the product.
     - `category` (str): Category of the product.
     - `price` (float): Price of the product.
     - `stock_quantity` (int): Current stock quantity.
   - **Methods**:
     - `update_stock(quantity: int) -> None`: Adjusts the stock quantity by a specified amount.
     - `display_details() -> None`: Prints product details.

3. **InventoryManagementSystem**: Core system that coordinates user authentication and product management.
   - **Attributes**:
     - `users` (Dict[str, User]): Dictionary to store registered users.
     - `products` (Dict[str, Product]): Dictionary to store products.
     - `current_user` (Optional[User]): Tracks the currently logged-in user.
   - **Methods**:
     - `add_user(username: str, password: str, role: str) -> None`: Adds a new user to the system.
     - `login() -> bool`: Authenticates a user based on input credentials.
     - `add_product() -> None`: Adds a new product (Admin only).
     - `view_products() -> None`: Displays all products with a low-stock alert if stock falls below the threshold.
     - `search_product() -> None`: Searches for products by name or category.
     - `edit_product() -> None`: Edits details of an existing product (Admin only).
     - `delete_product() -> None`: Deletes a product by ID (Admin only).
     - `logout() -> None`: Logs out the current user.
     - `run() -> None`: Main loop that runs the inventory management system and handles user input.

## Type Hints

The code uses type hints for enhanced readability and maintainability. Type hints specify the expected data types for function parameters and return values, ensuring consistency and aiding in debugging.

## Installation

1. Clone this repository or download the source code.
2. Make sure you have Python 3.6+ installed on your system.
3. Run the application with:
   ```bash
   python main.py

---
### Default User Credentials

- **Admin**
  - **Username**: `admin`
  - **Password**: `adminpass`

- **User**
  - **Username**: `user`
  - **Password**: `userpass`
---
