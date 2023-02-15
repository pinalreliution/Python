'''
Exercise: E001-V1
  Create one class named "category" with members "name", "code", "no_of_products"
  Create one class named "product" with members "name", "code", "category", "Price"
  Create three objects of category.
  Create 10 different products. Code must be unique.
  Print category info with its no_of_products
  Sort and Print products based on price ( Price High to Low and Low to High) with all details.
  Search product using its code.
'''

class Category:

    def __init__(self,name,code):
        self.name = name
        self.code = code
        self.no_of_products = 0

    def details(self):
        print("Product name :", self.name,'|',"code :", self.code,'|',"No.of products :",self.no_of_products)


class Product(Category):
    def __init__(self,name,code, category, price):
        self.name = name
        self.code = code
        self.category = category
        category.no_of_products += 1
        self.price = price

    def details(self):
        return  print("Product name :", self.name,'|', "Code :", self.code, '|' ,"Category :",self.category.name,'|' ,"Price :",self.price )

    @staticmethod
    def short_lth():
        for product in range(len(product_list)):
            for product1 in range(product + 1, len(product_list)):
                if product_list[product].price > product_list[product1].price:
                    product_list[product], product_list[product1] = product_list[product1], product_list[product]

        for product in product_list:
            product.details()

    @staticmethod
    def short_htl():

        for product in range(len(product_list)):
            for product1 in range(product + 1, len(product_list)):
                if product_list[product].price < product_list[product1].price:
                    product_list[product], product_list[product1] = product_list[product1], product_list[product]

        for product in product_list:
            product.details()

    @staticmethod
    def search_product_using_code():
        x = int(input("Enter the code:"))
        for product in product_list:
            if product.code == x:
                product.details()

# Three objects of Category
c1 = Category("Cosmetic", 1001)
c2 = Category("Shop", 2001)
c3 = Category("Hair_oil", 3001)


# Ten different products
p1 = Product("kajal", 101, c1, 150)
p2 = Product("Eyeliner", 102, c1, 200)
p3 = Product("Eyebrow_pencil", 103, c1, 250)
p4 = Product("Nail_art", 104, c1, 50)
p5 = Product("Nail_polish", 105, c1, 180)
p6 = Product("Lux", 201, c2, 45)
p7 = Product("Dove", 202, c2, 100)
p8 = Product("Dattol", 203, c2, 500)
p9 = Product("Keshking", 301, c3, 65)
p10 = Product("Bjajalmond", 302, c3, 170)

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

print(".........No.of product with details.........")
c1.details()
c2.details()
c3.details()


product_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]


#Sort and Print products based on price (Price High to Low and Low to High) with all details.
print(".......Sort and Print products based on price....... ")

print("*****Price Low to High*****")
print(Product.short_lth())

print("*****Price High to Low*****")
print(Product.short_htl())


#Search product using code
print("......Search product using code......")
Product.search_product_using_code()

