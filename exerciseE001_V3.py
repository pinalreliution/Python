'''
    Exercise: E001-V3 :
    Create one class named “location” with members “name”, “code”.  #done
    Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.  #done
    Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”.  #done
        This method will return all “movement” objects which belong to the passed “product” as an argument.     #done
    Add new members inside the product “stock_at_locations”.        #done
        This new member is a type of Dictionary, and it contains “location” as key and actual stock of that product on that location as value.  #done
    Create 4 different location objects.        #done
    Create 5 different product objects.     #done
    Move those 5 products from one location to another location using movement.
        Manage exceptions if product stock goes in -ve.
    Display movements of each product using the “movement_by_product” method.       #done
    Display product details with its stock at various locations using “stock_at_locations”.     #done
    Display product list by location ( group by location).      #done
'''


class Location:

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __repr__(self):
        return self.name

    # Display product list by location ( group by location)
    @staticmethod
    def sort(l_list):
        for loc in range(len(l_list)):
            for loc1 in range(loc + 1, len(l_list)):
                if l_list[loc].name > l_list[loc1].name:
                    l_list[loc], l_list[loc1] = l_list[loc1], l_list[loc]
        for loc in l_list:
            print("Location name:", loc.name)
            for product1 in mov_list:
                if loc == product1.from_location:
                    print("Product details :", "Name :", product1.product.name, '|', "Code :", product1.product.code,
                          '|', "Price :", product1.product.price, '|', "Stock of products :",
                          product1.product.stock_at_locations)
            print()

    def show_location(self):
        print("Location name : ", self.name, '\n', "Code : ", self.code)


class Movement:

    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        self.change_value()
        product.stock_at_locations.update({str(self.to_location.name): str(self.quantity)})
        # product.stock_at_locations.update({str(self.from_location): str(self.stock())})

    def change_value(self):
        for i, j in self.product.stock_at_locations.items():
            self.product.stock_at_locations[i] = j - self.quantity
            # raise Exception("Out of stock")
            # if self.quantity <= j:
            #     self.product.stock_at_locations[i] = j - self.quantity
            #     print(self.product.stock_at_locations[i])
            # else:
            #     raise Exception("Out of stock")

    # Display movements of each product using the “movement_by_product” method
    @staticmethod
    def movements_by_product(product):
        for pro in mov_list:
            if pro.product == product:
                pro.show_movement()

    def show_movement(self):
        print("From location : ", self.from_location.name, " ", "To ", self.to_location.name, '|',
              "Product :", self.product.name, '|', "Quantity :", str(self.quantity))


class Product:

    def __init__(self, name, code, price, stock_at_locations):
        self.name = name
        self.code = code
        self.price = price
        self.stock_at_locations = stock_at_locations

    def show_product(self):
        return print("Product name :", self.name, '|', "Code :", str(self.code), '|',
                     "Price :", str(self.price), '|', "Stock at locations :", self.stock_at_locations)


# Create location class object
rajkot = Location("Rajkot", 1001)
jamnagar = Location("Jamnagar", 2001)
ahmadabad = Location("Ahmadabad", 3001)
baroda = Location("Baroda", 4001)

# Create product class object
airconditioner = Product("Airconditioner", 101, 450000, {rajkot: 100})
cloths = Product("Cloths", 201, 3600, {jamnagar: 50})
chair = Product("Chair", 301, 890000, {ahmadabad: 30})
book = Product("Book", 401, 455874, {baroda: 50})
laptop = Product("Laptop", 501, 45789, {rajkot: 90})

# Create movement class object
m1 = Movement(rajkot, jamnagar, airconditioner, 78)
m2 = Movement(jamnagar, ahmadabad, cloths, 55)
m3 = Movement(ahmadabad, baroda, chair, 23)
m4 = Movement(baroda, rajkot, book, 41)
m5 = Movement(rajkot, ahmadabad, laptop, 85)

print()
print(".....Display movements of each product using the movement_by_product method.....")
mov_list = [m1, m2, m3, m4, m5]
Movement.movements_by_product(airconditioner)
Movement.movements_by_product(cloths)
Movement.movements_by_product(chair)
Movement.movements_by_product(book)
Movement.movements_by_product(laptop)

print()
print(".....Display product details with its stock at various locations using stock_at_locations.....")
airconditioner.show_product()
cloths.show_product()
chair.show_product()
book.show_product()
laptop.show_product()

print()
print("......Display product list by location ( group by location)......")
l_list = [rajkot, jamnagar, ahmadabad, baroda]
Location.sort(l_list)