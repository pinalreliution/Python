'''
    Exercise: E001-V3 :
    Create one class named “location” with members “name”, “code”.  #done
    Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.  #done
    Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”.  #done
        This method will return all “movement” objects which belong to the passed “product” as an argument.
    Add new members inside the product “stock_at_locations”.        #done
        This new member is a type of Dictionary, and it contains “location” as key and actual stock of that product on that location as value.
    Create 4 different location objects.        #done
    Create 5 different product objects.     #done
    Move those 5 products from one location to another location using movement.
        Manage exceptions if product stock goes in -ve.
    Display movements of each product using the “movement_by_product” method.
    Display product details with its stock at various locations using “stock_at_locations”.
    Display product list by location ( group by location).
'''


class Location:

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def show_location(self):
        print("Location name : ", self.name, "Code : ", self.code)


class Movement:

    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity

    @staticmethod
    def movements_by_product(product):
        x = input("Insert the product : ")
        if x == product:
            return Movement.show_movement()
        else:
            return print("Nothing")

    def show_movement(self):
        print("From location : ", self.from_location.name, '|', "To location :", self.to_location.name, '|',
              "Product :", self.product.name, '|', "Quantity :", self.quantity)


class Product:

    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price
        self.stock_at_locations = dict()

    def add(self, key, value):
        self.stock_at_locations[key] = value

    def details(self):
        return print("Product name :", self.name, '|', "Code :", self.code, '|',
                     "Price :", self.price, "Stock at locations :", self.stock_at_locations)


# Create product class object
p1 = Product("Airconditioner", 101, 450000)
p2 = Product("Cloths", 201, 3600)
p3 = Product("Chair", 301, 890000)
p4 = Product("Book", 401, 455874)
p5 = Product("Laptop", 501, 45789)

# Create location class object
l1 = Location("Rajkot", 1001)
l2 = Location("Jamnagar", 2001)
l3 = Location("Ahmadabad", 3001)
l4 = Location("Baroda", 4001)

# Create movement class object
m1 = Movement(l1, l2, p1, 78)
m2 = Movement(l1, l3, p2, 45)
m3 = Movement(l3, l4, p3, 23)
m4 = Movement(l2, l1, p4, 41)
m5 = Movement(l4, l3, p5, 85)


p1.add(l1.name, m1.quantity)
p2.add(l2.name, m2.quantity)
p3.add(l3.name, m3.quantity)
p4.add(l4.name, m4.quantity)
p5.add(l1.name, m5.quantity)

p1.details()
p2.details()
p3.details()
p4.details()
p5.details()

m1.show_movement()
m2.show_movement()
m3.show_movement()
m4.show_movement()
m5.show_movement()

Movement.movements_by_product(p2.name)