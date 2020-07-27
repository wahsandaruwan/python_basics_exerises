#display output
print('Hello World')

#User Input
ui = input("Enter a number : ")
print(ui)

#Numbers
a = 8
b = 10.123445564564564737375474576575676575675677675675675
print(a+b)

#Data Type
age = input('Enter your age : ')
newage = str(age)
print(newage + 5)

#Math
math = (20 - 10) / (5 * 3) ** 2
print(math)

#String
s = "Hello World"
print(s)

snew = s.replace("W","k", 7)
print(snew)

#Indexing
c = "Hello Lapaya"
print(type(c[2:5]))

#List
s = "Hello Lapaya"
c = ["Hello",12,"hhh",33.4,s,12]
c.append(112.88)
print(c)
c.remove("Hello")
print(c)
c.clear()
print(c)
c.pop(3)
print(c)

print(c.index("Hello"))
print(c.count(12))

k = [3,4,62,3,24,24,10]
print(k)
k.sort()
print(k)
k.reverse()
print(k)

i = ["My", "Name", "is", "Himal","bfg"]
print(i)
print(" ".join(i))

li = ["red","green","yellow","black","purple","brown"]
print(li)
print(li[1:5])

li1 = li[:]
print(li1)
print(li != li1)
print(li is li1)
print(li[:2])
print(li[1::2])
print(li[2::-1])
print(li[:2:-1])
print(li[::-1])

print(li1)
li1[1:1] = ['A','B','C']
print(li1)

names = ["Motari", "Bathali"]
print(names)
names[0],names[1] = names[1],names[0]
print(names)

#Tuple
t = (23,"chamara",45.55,'K',2.3455,2500,'K',3434,'K')
print(t)
print(t[-1])
print(t[2])
print(len(t))
print(t.count('K'))


#Set
s1 = set({1,3,5,6})
s2 = {6,8,9}
print(type(s1))
print(type(s2))

s3 = {1,2,4,5,6,5,4}
print(s3)

s1.add(7)
print(s1)

s1.remove(5)
print(s1)

s3.discard(5)
print(s3)

s4 = {1,2,3,4,5}
s5 = s4.copy()
print(s5)
print(s5 is s4)

s4.clear()
print(s4)

s6 = {9,8}
s6 = s4.copy()
print(s6)
print(s6 is s4)

#Dictionaries
d = {
    "First Name" : "Himal",
    "Last Name" : "Sandaruwan",
    "Age" : 25,
    "Locations" : ("Panadura","Nawala"),
    # "Phone" : {
    #     "Mobile" : 1324345,
    #     "Home" : 464645
    # }
}
print(d["First Name"])
print(d["Locations"])

print(d.keys())
print(d.values())

print(d.items())

print("First Nam" in d)

print("Sandaruwan" in d.values())

# d.clear()
# print(d)

di = dict(a=1,b=2,c=3,d=4)
print(di)
c = di.copy()
print(c)
print(c is di)

d["dob"] = "13/2/1995"
print(d)

del d["dob"]
print(d)

print(len(d))

d.pop('First Name')
print(d)

first = dict(a=1,b=2,c=3,d=4,e=5)
second = dict(k=5,f=12)
print(first)
print(second)
second.update(first)
print(second)

#Ranges
r = range(11)
print(list(r))

num = range(1,10,2)
print(list(num))