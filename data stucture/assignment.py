retry=True
# variable for user input
name=input("Please enter your name---------------->")
# while retry means the loop working for the retry at the bottom of the code
while retry:
    print(f"{name} Welcome to this platform")
    print("This platform tell you some good fact about our president that ruled us from 1999-till date")
    name=(input("Please input a president that ruled from 1999-till date ------------------>"))

    # name1 means the variable for the first president in 1999 

    name1=("Chief Olusegun Obasanjo","olusegun","obasanjo","obj","chief obasanjo","chief olusegun","olusegun obasanjo")

    # name2 means the variable for the second president in 2007

    name2=("Alhaji Umaru Musa Yar'Adua","alhaji musa","yaradua","alhaji umaru","musa yaradua","musa Yar'Adua","musa","alhaji")

    # name3 means the variable for the third president in 2012

    name3=("Dr.Goodluck Ebele jonathan","goodluck jonathan","ebele jonathan","goodluck","jonathan","goodluck  jonathan","ebele")

    # name4 means the variable for the fourth president in 2015

    name4=("Muhammadu Buhari","buhari","muhammadu")

    # name5 means the variable for the current president

    name5=("Asiwaju Bola Ahmed Tinubu","Bola Tinubu","tinubu","asiwaju bola ahmed tinubu","ahmed bola tinubu","bola ahmed","ahmed tinubu","asiwaju bola ahmed","bola ahmed tinubu")
    
    if str.lower(name) in  name1:
        print("Chief Olusegun Obasanjo: He brought telecommunication in Nigeria")
    elif str.lower(name) in name2:
        print("Alhaji Umaru Musa Yar'Adua: He  brought peace in the country ")
    elif str.lower(name) in name3:
            print("Dr.Goodluck Ebele jonathan: He maintain a steady price of essential commodities")
    elif str.lower(name) in name4:
            print("Muhammadu Buhari: He made transportation easy by railway")
    elif str.lower(name) in name5:
            print("Asiwaju Bola Ahmed Tinubu: He his still ruling ooooo")
    else:
        print("Misspelled word")
        
  
    choice= input("Do you want to retry? (yes/no):")
    if choice == "no":
        retry = False
    elif choice == "yes":
        print("Goodluck once again")   
    else:
        print("Invalid input, program terminated")
        break