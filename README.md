# Shopping_Cart_System

## Overview

This project implements a simple shopping cart system with Python classes. The system consists of four main classes: `Product`, `Category`, `ShoppingCart`, and `Inventory`. These classes interact to create and manage a shopping cart with products, categories, and inventory management. Additionally, there's a function to save data from instances of these classes into a JSON file.

## Class Descriptions

### 1. `Product`

- This class represents a product in the shopping cart system.
- Attributes:
  - `product_id`: Unique identifier for the product (integer).
  - `name`: Name of the product (string).
  - `description`: Description of the product (string).
  - `price`: Price of the product (integer).
  - `quantity_in_stock`: Quantity of the product in stock (integer).
  - `category_id`: Identifier for the category the product belongs to (integer).
- Provides getters for accessing product attributes.
- Includes a `__str__` method to display product information.

### 2. `Category`

- Represents a product category.
- Attributes:
  - `category_id`: Unique identifier for the category (integer).
  - `name`: Name of the category (string).
  - `ctg_list`: List to hold products belonging to this category.
- Provides getters to access category attributes.
- Includes methods to group products by category and retrieve a list of products in the category.
- Includes a `__str__` method to display category information.

### 3. `ShoppingCart`

- Represents a shopping cart for storing products.
- Attributes:
  - `cart`: List to store product names.
- Provides methods to add and remove products from the cart, calculate the total price, and display the cart's contents.
- Includes a `__str__` method to display the contents of the shopping cart.

### 4. `Inventory`

- Manages the inventory of products and categories.
- Attributes:
  - `products`: Dictionary to store product instances with product IDs as keys.
  - `categories`: Dictionary to store category instances with category IDs as keys.
- Provides methods to add and remove products and categories from the inventory.
- Includes a `__str__` method to display the list of categories and products in the inventory.

## Usage

1. Create instances of the `Product`, `Category`, `ShoppingCart`, and `Inventory` classes.
2. Add products to categories, add products to the shopping cart, and manage the inventory as needed.
3. Use the `SaveJson` function to store data from instances into a JSON file.

```python
# Create instances of classes and manage the shopping cart and inventory
p1 = Product(product_id=1, name="prod1", price=10, category_id=12, description="hahaha", quantity_in_stock=1)
c1 = Category(category_id=1, name="c21")
c2 = Category(category_id=12, name="c1")
sc = ShoppingCart()
inv = Inventory()

c1.groupbyCt(p1)
sc.add_to_cart(p1, 3)
inv.add_product(p1)
inv.add_categories(c2)

# Save data to a JSON file
SaveJson(products=[p1], categories=[c1, c2], shopping_cart=sc, inventory=inv)
```

## Data Storage

Data from instances of the classes (`Product`, `Category`, `ShoppingCart`, and `Inventory`) can be stored in a JSON file named `data.json`. The `SaveJson` function is responsible for converting the data into JSON format and saving it to the file.

## Note

This project serves as a basic implementation of a shopping cart system in Python and includes the capability to save data to a JSON file. Depending on the requirements, you can expand and enhance the functionality, such as implementing more advanced features like user authentication, database integration, and a graphical user interface (GUI) for better user interaction.
