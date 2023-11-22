import temperature_converter
fahrenheit=[]
converted=[]
while True:
    try:
        user_input=(input("Enter your Celsius temp to convert it into Fahrenheit or type done to stop: "))
        if user_input.lower() == 'done':
            break
        celsius= float(user_input)
        fahrenheit.append(celsius)
        # mmm=user_input.append(celsius)
        # user_input.append(celsius)
    except ValueError as error:
        # print("Please input A number")
        continue
print(fahrenheit)
for i in fahrenheit:
        
        conversion=temperature_converter.farenheit_to_celsius(i)
        nn=round(conversion,2)
        converted.append(nn)
print(converted)
    # else:
        # fahrenheit= temperature_converter.farenheit_to_celsius(celsius*9/5)+32
        # print (f"Your celsius temperature in Fahrenheit is {fahrenheit} " )
