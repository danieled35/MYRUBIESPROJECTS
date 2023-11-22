def partyguest():
    food=[]

    invited=[]

    while True:
        user_input=input("Enter a guest's name or type 'end' to stop.")

        if user_input == "end":
            break
        else:
            invited.append(user_input)
            print(f"{user_input} has been added to the guest list")
    name=len(invited)
    # print(name)
    cal=name*12
    # print(cal)
    for x in invited:
        print(x)
    print(f"you have invited {name} guest at the cost of ${cal}")
    return(invited)
print(partyguest())