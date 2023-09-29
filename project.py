import json


# class Product
class Product:

    # Constractor of product class

    def __init__(self, product_id: int, name: str, description: str, price: int, quantity_in_stock: int,
                 category_id: int):
        self.__product_id = product_id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__quantity_in_stock = quantity_in_stock
        self.__category_id = category_id

    # getters of instance of the class
    def getproduct_id(self):
        return self.__product_id

    def getname(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def getPrice(self):
        return self.__price

    def getQuantity_in_stock(self):
        return self.__quantity_in_stock

    def getCatgory_id(self):
        return self.__category_id

    # method to String of this class
    def __str__(self):
        return f"product_id: {self.getproduct_id()}, name: {self.getname()}, " \
               f"description: {self.getDescription()}, price: {self.getPrice()}," \
               f" quantity_in_stock: {self.getQuantity_in_stock()}, category_id: {self.getCatgory_id()}"


class Category:

    # Constractor of Category  class

    def __init__(self, category_id, name):
        self.__category_id = category_id
        self.__name = name
        self.ctg_list = []  # Initialize ctg_list as an empty list

    # Getters
    def get_category_id(self):
        return self.__category_id

    def getName_cat(self):
        return self.__name

    # Method to get the number of products by his category
    def groupbyCt(self, product):
        if self.get_category_id() == product.getproduct_id():
            self.ctg_list.append(product)
        else:
            print("Not in the same category")

    # Method tp get the list of products
    def list_of_products(self):
        return [product.getname() for product in self.ctg_list]

    # Method to string of this class

    def __str__(self):
        return f"category_id: {self.get_category_id()}, name: {self.getName_cat()}, " \
               f"product_list: {' '.join(self.list_of_products())}"


# Class ShoppingCart
class ShoppingCart:
    # Constractor of this class
    def __init__(self):
        self.__cart = []

    # Getters
    def getCart(self):
        return self.__cart

    # method to add products by quantity and append them in a list
    def add_to_cart(self, product, quantity):
        if product.getname() not in self.getCart():
            for i in range(quantity):
                self.getCart().append(product.getname())

    # method to remove products by quantity
    def remove_from_cart(self, product, quantity):
        if product.getname() in self.getCart():
            for i in range(quantity):
                self.getCart().remove(product.getname)

    # Method to calculate the price of all products and return total
    def Calculate(self, product):
        total = 0
        for _ in self.getCart():
            total += product.getprice()
        return "your total is " + str(total) + " $"

    # Mehtod to string of this class
    def __str__(self):
        return f"ProductList : {','.join(self.getCart())}"


# class inventory
class Inventory:
    # Constrcator
    def __init__(self):
        self.__products = {}
        self.__categories = {}

    # getters
    def getprodcuts(self):
        return self.__products

    def getcategories(self):
        return self.__categories

    # method to add products to the dict of products
    def add_product(self, product):
        if product.getproduct_id() not in self.getprodcuts():
            self.getprodcuts()[product.getproduct_id()] = product
        else:
            print("product is on the stock")

    # method to remove products to the dict of products
    def Remove_product(self, product_id):
        if product_id in self.getprodcuts():
            del self.getprodcuts()[product_id]

    # method to add categories to the dict of products
    def add_categories(self, category):
        if category.get_category_id() not in self.getcategories():
            self.getcategories()[category.get_category_id()] = category
        else:
            print("product is on the stock")

    # method to remove category to the dict of products

    def Remove_categories(self, category_id):
        if category_id in self.getcategories():
            del self.getcategories()[category_id]

    # method to string
    def __str__(self):
        return f"list of catgory {','.join(category.getName_cat() for category in self.getcategories().values())}\n"f"list of product {','.join(product.getname() for product in self.getprodcuts().values())}"


# Create instances of your classes
p1 = Product(product_id=1, name="prod1", price=10, category_id=12, description="hahaha", quantity_in_stock=1)
c1 = Category(category_id=1, name="c21")
c2 = Category(category_id=12, name="c1")
sc = ShoppingCart()
inv = Inventory()

# Add instances to your inventory and cart
c1.groupbyCt(p1)
sc.add_to_cart(p1, 3)
inv.add_product(p1)
inv.add_categories(c2)


# Modify SaveJson function to accept and save multiple instances
def SaveJson(products, categories, shopping_cart, inventory):
    data_to_save = {
        "products": {},
        "categories": {},
        "shopping_cart": {},
        "inventory": {}
    }

    # Save product instances
    for product in products:
        product_dict = {
            "product_id": product.getproduct_id(),
            "name": product.getname(),
            "description": product.getDescription(),
            "price": product.getPrice(),
            "quantity_in_stock": product.getQuantity_in_stock(),
            "category_id": product.getCatgory_id()
        }
        data_to_save["products"][product.getproduct_id()] = product_dict

    # Save category instances
    for category in categories:
        category_dict = {
            "category_id": category.get_category_id(),
            "name": category.getName_cat(),
            "product_list": category.list_of_products()
        }
        data_to_save["categories"][category.get_category_id()] = category_dict

    # Save shopping cart instance
    shopping_cart_dict = {
        "product_list": shopping_cart.getCart()
    }
    data_to_save["shopping_cart"] = shopping_cart_dict

    # Save inventory instance
    inventory_dict = {
        "categories": {category.get_category_id(): category.getName_cat() for category in inventory.getcategories().values()},
        "products": {product.getproduct_id(): product.getname() for product in inventory.getprodcuts().values()}
    }
    data_to_save["inventory"] = inventory_dict

    # Save the data to a JSON file
    with open("data.json", "w") as f:
        json.dump(data_to_save, f, indent=4)
        print("Data saved to data.json")

# Store data of instances
SaveJson(products=[p1], categories=[c1, c2], shopping_cart=sc, inventory=inv)



