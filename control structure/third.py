# Find Duplicate Elements in a list

num=[1,2,3,4,5,2,3,4,7,9,5,7,9,7,10,10]
unknown=[]
for i in num:
    if i not in unknown:
        unknown.append(i)
    else:
        print(i,end=' ')

  