a=200
b=99
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")
#elif operator-if previous condition not true try this one
a=200
b=200
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
#while loops
i=1
while i<10:
    print(i)
    i=i+1
#for loops
letters=["a","b","c","d","e"]
for x in letters:
    print(x)
#range function
for y in range(6):
    print(y)

for z in range(2,6):
    print("hii")

for a in range(0,100,10):
    print(a)
# break
fruits = ["apple", "orange", "cherry","banana","mango"]
for o in fruits:
    print(o)
    if o == "banana":
        break

#relational operators in python <,>,<=,>=<,!=,==
print(5!=5)
print(3<=4)
print(4>=4)

#logical operators
if(1<2 and 5>3):
    print("both conditions are true")
else:
    print("one of the condition is false")

if(1>2 and 5>3):
    print("both conditions are true")
else:
    print("one of the condition is false")

if(1>2 or 5>3):
    print("one of the condition is true")
else:
    print("both conditions are false")

if(1>2 or 5<3):
    print("one of the condition is true")
else:
    print("both conditions are false")
