# convert list to set
# items=["books","candles","pens","pencils","jotter"]
# item2=set(items)
# print(item2)

# add and removal of set
# items={"books","candles","pens","pencils","jotter"}
# items.discard("egg") #to remove from a set
# print(items)

# union
# items={"books","candles","pens","pencils","jotter"}
# items2={"tropical","oranges","apples","mangoes"}
# items_union=items | items2
# print(items_union)


# intercept
# items={"books","candles","pens","pencils","jotter","apples"}
# items2={"tropical","oranges","apples","mangoes"}
# items_intercept=items & items2
# print(items_intercept)

# set difference
# items={"books","candles","pens","pencils","jotter","apples"}
# items2={"tropical","oranges","apples","mangoes"}
# items_difference=items - items2
# print(items_difference)


# items={"books","candles","pens","pencils","jotter","apples"}
# items2={"tropical","oranges","apples","mangoes"}
# items_method=items ^ items2
# # print(items_method)

items={"books","candles","pens","pencils","jotter","apples"}
items2={"tropical","oranges","apples","mangoes"}
items_union =items | items2
# for y in items_union:
#     print(y)
vary={ y * y for y in range(1,10)}
print(vary)