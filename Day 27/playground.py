# arguments : *args

def add(*args):
    print(args[1])
    sum =0
    for i in args:
        sum += i
    return sum
    # print(type(args))

print(add(3,4,6,8,4,25,8,9,7,5,3,7,5,3,))

# **kwargs

def calculate(n, **kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3, multiply=5)

class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Ford")
print(my_car.make)
print(my_car.model)