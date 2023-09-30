retry=True
while retry:
    a=("carbohydrate")
    b=("protein")
    c=("vitamin")
    d=("fats and oil")
    e=("minerals salt")
    f=("water")
    p=("rice","cereals")
    try:
        g=str(input("Please input your preferred food"))
        if g==p:
            print(f"The food is a {a}")
        else:
            if g==b:
                print("sdfghj") 
    except  ValueError:
        print("ftgyhgjhkj")
    choice= input("Do you want to retry? (yes/no):")
    if choice == "no":
        retry = False
    elif choice == "yes":
        print("Goodluck once again")   
    else:
        print("Invalid input, program terminated")
        break
    