"#tuples is a sequence of immutable pyhton objects i.e we cannot change it's values#"
#creating a tuple#
tuple1=('a','b','c','d','e')
print(tuple1)
#another way of creating a tuple#
tuple2='abc',12,'def',34
print(tuple2)
#nesting of tuples#
tuple3=(tuple1,tuple2)
print(tuple3)
#repetition of tuples#
tuple4=('python',)*4
print(tuple4)
#immutable tuples#
tuple1[2]='z'
print(tuple1)#it gives an error as tuples are immutable#
#slicing in tuples#
tuple5=('C',0,'Java',1,'Pyhton',2,'PHP',3)
print(tuple5[0:3])
print(tuple5[2:5])
print(tuple5[::-1])#printed in reverse order#
#length of a tuple#
print(len(tuple5))
#deleting a tuple#
tuple6=(1,2,3,4)
del tuple6
print(tuple6)#it will give an error#