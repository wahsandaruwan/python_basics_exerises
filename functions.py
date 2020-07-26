# User Defined Functions
def example():
    print("Hello World!")
    print("Age : " + str(25))

example()

def minutes_to_hours(minutes):
    hours = minutes/60
    return hours

print(minutes_to_hours(80))

def full_name(fname,lname):
    return(f"Your name is {fname} {lname}")

print(full_name("Kasun","Perera"))

def km_to_m(km):
    meters = km * 1000;
    return meters

# print(km_to_m(int(input("Enter the distance in KM : "))))

def m_to_cm(ui):
    cm = km_to_m(ui) * 100
    return cm

print(m_to_cm(int(input("Enter the distance in KM : "))))

def min_to_hour(minutes,second = 250):
    hours = (minutes/60) + (second/3600)
    return hours

print(min_to_hour(500))

def exponent(number=5,power=4):
    return number ** power

print(exponent(2,4))
print(exponent(20,20))
print(exponent())
print(exponent(10))

def add(a,b):
    return a+b

def math(a,b,fn=add):
    return fn(a,b)

def sub(a,b):
    return a-b

print(math(2,3))
print(math(1,3,sub))

def full(first,last):
    return f"Your name is {first} {last}"

print(full(last="Perera", first="Chamara"))

# Global Variables
instant = "Himal"
total = 0
def sample():
    print(total)
    return f"Hello {instant}"

print(sample())
print(instant)

def inc():
    global total
    total = total + 1
    return total

print(inc())

# Local/Parent Variable
def simple():
    count = 0
    print(count + 5)

simple()

def simple2():
    sum = 5
    def inner():
        nonlocal sum
        sum = sum + 5
        return sum
    return inner()
    
print(simple2())