num = [1,2,3,4,5]
num1 = [1,2,3,4,5,6,7,8,9]
print(type(num))
print(type(num1))

class User:
    pass

user1 = User()
user2 = User()
print(user1)
print(type(user1))

class User:
    def __init__(self):
        print("Hello World!")

user1 = User()
user2 = User()

class User:
    def __init__(self,first,last,age):
        self.fname = first
        self.lname = last
        self.age = age

user1 = User("Kasun", "Perera", 24)
print(user1.fname,user1.lname)

user2 = User("Dasun", "Silva", 34)
print(user2.fname,user2.lname)

class Person:
    def __init__(self):
        self.name = "Himal"
        self._age = 25
        self.__msg = "Hello!"
        self.__email = "dfdff@sfsf.lk"

person = Person()
print(person.name)
print(person._age)
print(person._Person__msg)

class User:
    def __init__(self,first,last,age):
        self.fname = first
        self.lname = last
        self.age = age

    #Instance Methods
    def fullname(self):
        return f"{self.fname} {self.lname}"

    def initials(self):
        return f"{self.fname[0]}.{self.lname[0]}."

    def likes_to_eat(self,food):
        return f"{self.fname} likes to eat {food}"

    def is_old(self):
        return self.age >= 30

user1 = User("Himal","Sandaruwan",25)
user2 = User("Kasun","Perera",22)

print(user1.fullname())
print(user2.initials())
print(user1.likes_to_eat("Chocolate"))
print(user2.is_old())
print(user1.age)

# Inheritance

class Animal:
    ok = True
    def make_sound(self,sound):
        print(f"This animal says {sound}")

class Cat(Animal):
    def eat(self,what):
        print(f"It eats {what}")

class Cub(Cat):
    pass

a = Animal()
b = Cat()
c = Cub()

b.make_sound("Meow")
print(b.ok)

c.eat("Fish")
c.make_sound("Meow")

# Encapsulation
class Human:
    def __init__(self,first,last,age):
        self.fname = first
        self.lname = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    def get_age(self):
        return self._age

    def set_age(self,newage):
        if newage >= 0:
            self._age = newage
        else:
            self._age = 0

kasun = Human("Kasun", "Silva", 26)
# #print(kasun._age)
print(kasun.get_age())
kasun.set_age(30)
print(kasun.get_age())

# Polymorphism
# 1. Method Overriding
class Animal:
    def sound(self):
        raise NotImplementedError("Subclass need to implement this method")
class Dog(Animal):
    def sound(self):
        return "Woof!!!"

class Cat(Animal):
    def sound(self):
        return "Meow!!!"

class Fish(Animal):
    pass

d = Dog()
print(d.sound())

f = Fish()
print(f.sound())

a = Animal()
print(a.sound())


# 2. Method Overloading
from multipledispatch import dispatch
# pip install multipledispatch
class Example():

    @dispatch(int,int)
    def warranty(self,a,b):
        w = a + b
        print(w)

    @dispatch(int,int,int)
    def warranty(self,a,b,c):
        qt = a + b + c
        print(qt)
    
    @dispatch(int,int,float)
    def warranty(self,a,b,c):
        k = a + b + c
        print(k)

obj = Example()
obj.warranty(2,4)
obj.warranty(2,4,6)
obj.warranty(2,4,23.4)
