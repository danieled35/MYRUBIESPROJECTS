# create a list and sum up the element in the list

mylist=[1,2,3,4,5,6,7,8,9]
# print(mylist)
list_lenth=len(mylist)
total=0
for i in range(list_lenth):
    total=total+mylist[i]

print(total)


# create a table and give the average of the elements in the tuple
mytuple=(1,2,3,4,5,6,7,8,9)
print(sum(mytuple)/len(mytuple))


# sum of product using dictionary
product={}
product["soap"]={"price":2000,"quantity":50}
product["milo"]={"price":9000,"quantity":70}
product["Biscuit"]={"price":1000,"quantity":60}
nn=0
for key,value in product.items():
    # print(value)
    # print(key)
    latest=value["price"]
    # print(latest)
    new=value["quantity"]
    # print(new)
    next = latest+new
    # print(next)
    nn += next
print(nn)