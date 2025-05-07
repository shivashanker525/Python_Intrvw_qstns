

class Base:
    __a = 23
    def add_num(self):
        print("Add numbers")
        print(self.__a)

    def __sub_num(self):
        print("SUbtraction numbers")
        print(self.__a)
    
a = Base()
a.add_num()
# a.__a
a.__sub_num()