retry=True
name=input("Please enter your name---------------->")
while retry:
    print(f"{name} Welcome to this platform")
    print("This platform tell you some good fact about  president")
    print("We tell you about some fact of  president like:Chief Olusegun Obasanjo,Alhaji Umaru Musa Yar'Adua,Dr.Goodluck jonathan,Muhammadu Buhari,Bola Tinubu")
    print("Please the president should be written in the correct  order above ")
    name=str(input("Please input a president that ruled from 1999-till date ------------------>"))
    name1=("Chief Olusegun Obasanjo")
    name2=("Alhaji Umaru Musa Yar'Adua")
    name3=("Dr.Goodluck jonathan")
    name4=("Muhammadu Buhari")
    name5=("Bola Tinubu")
    
    if name == str.lower("CHIEF Olusegun Obasanjo") in name1:
        print("He brought telecommunication in Nigeria")
    else:
        if name ==name2:
            print("He brought peace in the country ")
        if name==name3:
            print("He maintain a steady price of essential commodities")
        if name==name4:
            print("He made transportation easy by railway")
        if name==name5:
            print("he his still ruling ooooo")
        
  
    choice= input("Do you want to retry? (yes/no):")
    if choice == "no":
        retry = False
    elif choice == "yes":
        print("Goodluck once again")   
    else:
        print("Invalid input, program terminated")
        break 