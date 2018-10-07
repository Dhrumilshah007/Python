#list is a collection which is ordered and changeable.List are written with square brackets.
#creating a list
list1=['C','C++','Java','Python']
print(list1)
#accessing items of the list
print(list1[2])
#print(list1[4])#will give an error
#changing values in list
list1[2]='PHP'
print(list1)
#length of list
print(len(list1))
#loop through the list
for x in list1:
    print(x)
#adding items in the list
list1.append('R')#add an item at the end of the list
print(list1)
#adding an item at specified index
list1.insert(1,'Perl')
print(list1)
#remove items from list
#remove() method removes the specified item
list2=['red','orange','yellow','pink']
print(list2)
list2.remove('red')
print(list2)
#pop() removes the specified index or last item if index not specified
list3=['red','orange','yellow','pink']
print(list3)
list3.pop()
print(list3)
# del keyword removes the specified index and delete the list completely
list4=[1,2,3,4,5,6]
print(list4)
del list4
print(list4)#cause an error as list4 no longer exists
