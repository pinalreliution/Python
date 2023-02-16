'''
Exercise: E001-V2
● Add new data members “parent”, “display_name”, “products” (list of product objects)
inside category class.
● Add a new member function to generate “display_name”.
● “display_name” has text value as below.
     Vehicle category without parent then “Vehicle”
     Car category with “Vehicle” as parent then “Vehicle > Car”
     Petrol category with “Car” as parent then “Vehicle > Car > Petrol”
● Create 5 category objects with parent and child relation.
● Create 3 product objects in each category.
● Display Category with its Code, Display Name and all product details inside that
category.
● Display product list by category ( group by category, order by category name).
'''

class Category:

    def __init__(self, name, code, parent):
        self.name = name
        self.code = code
        self.parent = parent
        self.display_name = None
        self.products = None
        self.no_of_products = 0

    def display_name(self):
        while Category:
            print(self.parent)


    def details(self):
        print("Product name :", self.name,'|',"code :", self.code,'|',"No.of products :",self.no_of_products,'|',"Parent :",self.parent,'|',"Display name:",self.display_name,'|',"Products :",self.products)

class Product(Category):

    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        category.no_of_products += 1
        self.price = price

    def details(self):
        return  print("Product name :", self.name,'|', "Code :", self.code, '|' ,"Category :",self.category.name,'|' ,"Price :",self.price )


# Create 5 category objects with parent and child relation.
c1 = Category("Truck", 1001)
c2 = Category("Bus", 2001)
c3 = Category("Car", 3001)
c4 = Category("Bike", 4001)
c5 = Category("Cycle", 5001)

# Create 3 product objects in each category.
p1 = Product("Honda-city", 301, c3, 10000)
p2 = Product("Hero-honda", 401, c4, 50000)
p3 = Product("Mahindra", 101, c1, 4500)
p4 = Product("Egele", 201, c2,85000)
p5 = Product("Atlas", 501, c5, 1200)
p6 = Product("Suzuki", 302, c3, 9874)
p7 = Product("Activa", 402, c4, 1478)
p8 = Product("Tata", 102, c1,456874)
p9 = Product("Patel", 202, c2, 56741)
p10 = Product("Avon", 502, c5, 48)
p11 = Product("Verna", 303, c3, 1464)
p12 = Product("Plesure", 403, c4, 468932)
p13 = Product("Ashok-layland", 103 ,c1, 1564)
p14 = Product("Pramukhraj", 203, c2, 156)
p15 = Product("Firefox", 503, c5, 145)

pro_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15]

c1.details()
c2.details()
c3.details()
c4.details()
c5.details()

p1.details()
p2.details()
p3.details()
p4.details()
p5.details()
p6.details()
p7.details()
p8.details()
p9.details()
p10.details()
p11.details()
p12.details()
p13.details()
p14.details()
p15.details()
