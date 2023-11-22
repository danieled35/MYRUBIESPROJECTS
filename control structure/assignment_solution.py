carbohydtates=("rice","yam","cereals")
protein=("egg","beans")
vitamins=("meat","fish")
user_input=input("please enter your preferred food")
if str.lower(user_input) in carbohydtates:
    print(f"{user_input} belongs to class carbohydrate")
elif str.lower (user_input) in protein:
        print(f"{user_input} belongs to class protein")
elif str.lower(user_input) in vitamins:
      print(f"{user_input} belongs to class vitamins")