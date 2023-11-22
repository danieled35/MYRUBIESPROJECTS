def cslculator(user_input):
    # print(user_input)
    scores=0
    a=user_input.split(' ')
    # print(a)
    if "+" in a:
        scores=int(a[0])+int(a[2])
    elif "-" in a:
        scores=int(a[0])-int(a[2])
    if "*" in a:
        scores=int(a[0])*int(a[2])
    if "/" in a:
        scores=int(a[0])/int(a[2])
    # print(scores)
    return(scores)


user_input=input("please enter an expression")
print(cslculator(user_input))


