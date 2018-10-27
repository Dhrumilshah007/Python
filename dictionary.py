#key value pair in which we can access value using key

family={"dad":"bob","mom":"marry","brother":"james"}
#accessing items
print(family["dad"])
#updating values
family["dad"]="john"
print(family["dad"])
#adding items
family["sister"]="eli"
print(family)
#length of dictionary
print(len(family))
#delete value in the dictionary
del family["sister"]
print(family)
#get all the keys
print(family.keys())
#get all the values
print(family.values())
#add values to dictionary
family1={"ages":25,"houses":2}
family.update(family1)
print(family)
#clear everything in  dictionary
family.clear()
print(family)
