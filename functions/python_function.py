# def fav_food(a,b):
#     return(a)

# print(fav_food("rice","beans"))

# def name(a,b ):
#     mm=a+b
#     return(mm)
# print(name (2,2))


# def rectangle(a,b,c):
#     mmm=a/2 *b*c
#     return(mmm)
# print(rectangle(1,4,5))

def number(score):

    # grade=""
    if score>=75:
        grade="A"                                                                                                                                                                                                                                                                                                                                                                                                                            
    elif score >=65:
        grade="B"
    elif score >=60:
        grade="C"
    elif grade >=50:
        grade="D"
    elif score >=0:
        grade="F"
    else:
        ("Invalid score")

    return(grade)
print(number(100))

