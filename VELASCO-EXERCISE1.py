#John Michael Luis Velasco BSCPE 2-3
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    try:
        
        temperature = float(input("Enter the temperature value: "))
         
        print("Select the conversion type:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        choice = input("Enter 1 or 2: ")

        if choice == '1':

            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {result:.2f}°F")
        elif choice == '2':
        
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F is equal to {result:.2f}°C")
        else:
            print("Invalid choice! Please enter 1 or 2.")
    except ValueError:
        print("Please enter a valid number for the temperature.")

temperature_converter()
