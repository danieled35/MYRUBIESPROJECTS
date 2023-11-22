# the largest number on a tuple
first=(1,20,3,4,5,6,7,8,9,10)

larg=int(first[0])
for p in first:
    if p >larg:
        larg=p
     

print(larg)


