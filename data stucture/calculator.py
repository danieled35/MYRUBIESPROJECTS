# odd=(1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31)
# plus=(2,4,6,8,10,12,14,16,18,20,22,24,26,28,30)
# user_input=int(input("please enter a number"))
# if user_input in odd:
#     print(f"{user_input} is an odd number")
# elif user_input in plus:
#     print(f"{user_input} is an even number")
# even and odd number
# user_input=int(input("please enter a number"))
# if (user_input%2) ==0:
#     print("the number is even")
# else:
#     print("the number is odd")
# user_input=input("please enter your operation")
# newlist=user_input.split("+")
# total=0
# for total  in  int(newlist[0]):
#     print(total)



# user_input=int("enter a mathematical expression")2+2
# print(int(user_input))
# # user_input.split[user_input]
# if + in user_input:

user_input=input("please enter an expression")
print(user_input)
ans=0
a=user_input.split( )
print(a)
if "+" in a:
    ans=int(a[0])+int(a[2])
elif "-" in a:
    ans=int(a[0])-int(a[2])
if "*" in a:
    ans=int(a[0])*int(a[2])
if "/" in a:
    ans=int(a[0])/int(a[2])
print(ans)