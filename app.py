class Parent:
    def __init__(self, first_name, last_name):
        self.first_name= first_name
        self.last_name=last_name

    def print_name(self):
        print(self.first_name +' '+ self.last_name)


# parent = Parent('Ram', 'Kumar')

# parent.print_name()

class Child(Parent):
    def __init__(self, first_name, last_name):
        # self.first_name = first_name
        # self.last_name=last_name
        super().__init__(first_name, last_name)
 

child = Child('Ajay', 'Kumar')

# x = child.print_name()
# print(x)


class Computer:
    def __init__(self, price):
        # self.price=price
        self.__price=price
    def print_price(self):
        print(self.__price)
    def set_price(self, price):
        self.__price=price

c = Computer(100)

c.__price=200

c.set_price(500)

c.print_price()