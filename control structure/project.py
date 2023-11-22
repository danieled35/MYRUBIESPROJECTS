retry=True
while retry:
    print("Welcome to the simple interest platform")
    print("This platform helps to allow you calculate your simple interest with ease")
    principal=int(input("Please enter your principle amount"))
    rate=int(input("Enter your rate"))
    Time=int(input("Enter your estimated time"))
    simple_interest=principal*rate*Time/100
    print(f"Your simple interest is:{simple_interest}")



    choice= input("Do you want to re-calculate? (yes/no):")
    if choice == "no":
        retry = False
    elif choice == "yes":
        print("Goodluck once again")   
    else:
        print("Invalid input, program terminated")
        break
    