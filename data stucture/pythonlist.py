# list slicing
item=["apples","eggs","beans","rice","mango","oranges","banana","cherry"]
b=item[1:7:2]
print(b)

# string length
#  length fruit
b=len(item)
print(b)


# last item in a list
item=["apples","eggs","beans","rice","mango","oranges","banana","cherry"]
b=item[-1]
print(b)

# modifying list items
item=["apples","eggs","beans","rice","mango","oranges","banana","cherry"]
item[2]="plantain"
item[5]=500
item[7]=False
print(item)
# to add to a list
item.append("garri")
print(item)

# # to remove an item from a list
item.remove("rice")
print(item)

item=["apples","eggs","beans","rice","mango","oranges","banana","cherry"]
for item in item :
    print(item)
for i in range(1,13):
    print(8 * i )


# list concatenation
item=["apples","eggs","beans","rice","mango","oranges","banana","cherry"]
i=["english","math"]
result=item+i
print(result)


# Project1  
# Reversing a list
str="my name is daniel"
print(str[::-1])
# [::-1]) means reversing strings,list or any iterble with an ordering

# Project2
# iterating list
colour=["red","yellow","green"]
fruits=["apples","banana","mango"]
price=[60,20,80]
for colour,fruits,price in zip (colour,fruits,price):
    print(colour,fruits,price)
# zip is an in-built function in python used to iterate over multiple iterables
# iterables is an object which can be looped over.