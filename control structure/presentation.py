print("----- Welcome to EcoWarrior ------")
print("Please choose an option:")
print("1. What is plastic waste?")
print("2. Effects of plastic waste")
print("3. Tips to reduce plastic waste")
print("4. Exit")


while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Plastic waste, or plastic pollution, is the accumulation of plastic objects (e.g.: plastic bottles and much more) in the Earth’s environment that adversely affects wildlife, wildlife habitat, and humans.")
        
    elif choice == "2":
        print("Unlike other materials, plastic does not biodegrade. It can take up to 1,000 years to break down, so when it is discarded, it builds up in the environment until it reaches a crisis point. This pollution chokes marine wildlife, damages soil and poisons groundwater, and can cause serious health impacts.")
    elif choice == "3":
        print("The simplest way to reduce plastic waste is to avoid unnecessary and single-use plastics, support businesses who are reducing plastic waste and re-use existing plastic. Say no to disposable plastic cutlery, plastic straws and other single-use plastics. Avoid plastics that cannot be recycled if other alternatives exist.")
    elif choice == "4":
        print("Thank you for using EcoWarrior!")
        break
    else:
        print("Invalid choice. Please try again.")







