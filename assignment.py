names=["daniel","weijfodj0d"]

while True:
    user_input=input(" please enter your name ").strip()
    for name in names:
        if name == user_input.lower():
            print("user exist")
            break
        else:
            names.append(user_input.lower())
            print(user_input)
    # print(names)

