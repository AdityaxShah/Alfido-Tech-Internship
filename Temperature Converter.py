def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    
    choice = input("Enter choice (1/2/3/4/5/6): ")
    temp = float(input("Enter temperature: "))
    
    if choice == '1':
        print(f"{temp} °C = {temp * 9/5 + 32} °F")
    elif choice == '2':
        print(f"{temp} °C = {temp + 273.15} K")
    elif choice == '3':
        print(f"{temp} °F = {(temp - 32) * 5/9} °C")
    elif choice == '4':
        print(f"{temp} °F = {(temp - 32) * 5/9 + 273.15} K")
    elif choice == '5':
        print(f"{temp} K = {temp - 273.15} °C")
    elif choice == '6':
        print(f"{temp} K = {(temp - 273.15) * 9/5 + 32} °F")
    else:
        print("Invalid input!")

temperature_converter()
