########## Instance Attributes ##########

class Item:
    def __init__(self):
        print("I am Created!!!!")

    def calculate_price_of_item(self, x, y):
        return x * y
    
item1 = Item()
item1.name = "iphone"
item1.quantity = 100
item1.price = 18

item2 = Item()
item2.name = "samsung phone"
item2.quantity = 1000
item2.price = 47

########## with dynamic attributes ##########

class Item:
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def cal_price(self,x,y):
        return x * y

item1 = Item("oppo",600,90)
item2 = Item("iphone",6000,9)

print(item1.name)
print(item1.quantity)
print(item1.price)

print(item2.name)
print(item2.quantity)
print(item2.price)

########## with default values ##########

class Item:
    def __init__(self,name,price,quantity=0):
        self.name = name
        self.quantity = quantity
        self.price = price

    def cal_price(self,x,y):
        return x * y

item1 = Item("oppo",90)
item2 = Item("iphone",9)

print(item1.name)
print(item1.quantity)
print(item1.price)

print(item2.name)
print(item2.quantity)
print(item2.price)

########## method without parameters ##########

class Item:
    def __init__(self,name,price,quantity=0):
        self.name = name
        self.quantity = quantity
        self.price = price

    def cal_price(self):
        return self.price * self.quantity

item1 = Item("ios",56000,10)
print(item1.cal_price())

item2 = Item("andorid",25000,25)
print(item2.cal_price())

########## With type casting ##########

class Item:
    def __init__(self,name:str,price:float,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def cal_price(self):
        return self.quantity * self.price
    
item1 = Item(1,"nikhil")

########## Validation over arguments ##########

class Item:
    def __init__(self,name:str,price:float,quantity=0):

        assert price >= 0, f"Price is not greater then 0 entered value is {price}"
        assert quantity >= 0, f"Quantity is not greater then 0 entered value is {quantity}"

        self.name = name
        self.price = price
        self.quantity = quantity

    def cal_price(self):
        return self.quantity * self.price

item1 = Item("vivo",10,1000)
print(item1.cal_price())

############## Class Attributes ##############

class Item:

    pay_rate = 0.8

    def __init__(self,name:str,price:float,quantity=0):

        assert price >= 0, f"Price is not greater then 0 entered value is {price}"
        assert quantity >= 0, f"Quantity is not greater then 0 entered value is {quantity}"

        self.name = name
        self.price = price
        self.quantity = quantity

    def cal_price(self):
        return self.quantity * self.price
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("vivo",100,2)
item1.apply_discount()
print(item1.price)

item2 = Item("iphone",100,2)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

print(Item.pay_rate)
print(item1.pay_rate)
print(Item.__dict__)
print(item1.__dict__)

############## All attributes ##############

class Item:

    pay_rate = 0.8
    all = []
    def __init__(self,name:str,price:float,quantity=0):

        assert price >= 0, f"Price is not greater then 0 entered value is {price}"
        assert quantity >= 0, f"Quantity is not greater then 0 entered value is {quantity}"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def cal_price(self):
        return self.quantity * self.price
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item ({self.name},{self.quantity},{self.price})"

item1 = Item("phone",100,10)
item2 = Item("laptop",10,5)
item3 = Item("mouse",105,15)
item4 = Item("keyboard",19,19)
item5 = Item("cable",1000,10)

print(Item.all)

for instance in Item.all:
    print(instance.name,instance.quantity)


########### Instantiate from csv using class method ##########

import csv

class Item:

    pay_rate = 0.8
    all = []
    def __init__(self,name:str,price:float,quantity=0):

        assert price >= 0, f"Price is not greater then 0 entered value is {price}"
        assert quantity >= 0, f"Quantity is not greater then 0 entered value is {quantity}"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def cal_price(self):
        return self.quantity * self.price
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_class(cls):
        with open('/Users/nikhil/Desktop/DSA/Object Oriented Programming/items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = int(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    def __repr__(self):
        return f"Item ({self.name},{self.quantity},{self.price})"
    
Item.instantiate_from_class()
print(Item.all)

########### static method to check data type ##########

import csv

class Item:

    pay_rate = 0.8
    all = []
    def __init__(self,name:str,price:float,quantity=0):

        assert price >= 0, f"Price is not greater then 0 entered value is {price}"
        assert quantity >= 0, f"Quantity is not greater then 0 entered value is {quantity}"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def cal_price(self):
        return self.quantity * self.price
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_class(cls):
        with open('/Users/nikhil/Desktop/DSA/Object Oriented Programming/items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = int(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item ({self.name},{self.quantity},{self.price})"
    
print(Item.is_integer(1))
print(Item.is_integer(1.0))
print(Item.is_integer(1.7))

########### Inheritance ##########

class Phone(Item):
    def __init__(self,name:str,price:float,broken_phones,quantity=0):

        assert price >= 0, f"Price is not greater then 0 entered value is {price}"
        assert quantity >= 0, f"Quantity is not greater then 0 entered value is {quantity}"
        assert broken_phones >= 0, f"Broken phones is not greater than 0 and entered value is {broken_phones}"

        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones

phone1 = Phone("new_phone",10,7500,0)
print(phone1.apply_discount())
print(phone1.cal_price())

########### Inheritance with Super function to eliminate duplications ##########

class Phone(Item):
    def __init__(self,name:str,price:float,broken_phones,quantity=0):

        super().__init__(name,price,quantity)

        assert broken_phones >= 0, f"Broken phones is not greater than 0 and entered value is {broken_phones}"

        self.broken_phones = broken_phones

phone1 = Phone("new_phone",10,7500,0)
print(phone1.apply_discount())
print(phone1.cal_price())



