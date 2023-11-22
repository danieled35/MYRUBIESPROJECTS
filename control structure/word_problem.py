inventory={}
inventory["cream"]={"price":3000,"quantity":50}
inventory["Perfume"]={"price":5000,"quantity":40}
inventory["Milo"]={"price":1000,"quantity":90}
# print(inventory)
# calculations
cal=0
for key,value in inventory.items():
    # print(value)
    # print(key)
    # print(inventory["cream"])
    mm=value["price"]
    # print(mm)
    zz=value["quantity"]
    # print(zz)
    total=mm*zz
    print(total)
    cal=cal+total
print(cal)