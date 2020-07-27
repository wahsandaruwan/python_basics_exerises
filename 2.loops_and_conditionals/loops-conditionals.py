#loops & Conditionals

# For Loop
emails = ['123@gmail.com','45455@yahoo.com','fhgh@gmail.com','yuyu3@gmail.com','yty@gmail.com','35fd@yahoo.com']
for em in emails:
    print(em)

for em in emails:
    # if em.__contains__("gmail"):
    #     print(em)
    if 'gmail' in em:
        print(em)

number = [1,2,3,4,5]
dm = []
for num in number:
    dn = num * 2
    dm.append(dn)
    print(dn)

#List Comprehension
dm = [x*2 for x in number]
print(dm)

cat = ('A','B','C','D','E','F')
for c in cat:
    print(c)

for r in range(1,20,2):
    print(r)

--------------------
play = {
    "title" : "New Angel",
    "Author" : "Chamara Silva",
    "songs" : [
        {
            "title" : "song1",
            "artist" : ["blue", "kime"],
            "duration" : 3.2
        },
        {
            "title" : "song2",
            "artist" : ["nina"],
            "duration" : 3.5
        },
        {
            "title" : "song3",
            "artist" : ["wayne"],
            "duration" : 2.8
        }
    ]
}
for song in play["songs"]:
    print("Title - " + song["title"] + " | " + str(song["duration"]))

# While Loop
cat = ("jan","feb","mar","apr","may")
i = len(cat) - 1
while i >= 0:
    print(cat[i])
    i -= 1 # i = i - 1

j = 1
while j < 13:
    print("\U0001f600" * j)
    j = j + 1

# Conditionals
a = 6
if a < 7:
    print("a is less than 7")
elif a <= 9:
    print("a is less than or equal 9")
else:
    print("dfdfvdfbb")

print("dfgdfb")

