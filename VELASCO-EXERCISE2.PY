#John Michael Luis Velasco BSCPE 2-3
def calculate_voltage(current, resistance):
    return current * resistance

def calculate_current(voltage, resistance):
    return voltage / resistance

def calculate_resistance(voltage, current):
    return voltage / current

def ohms_law_calculator():
    print("Welcome to the Ohm's Law Calculator!")
    print("What would you like to calculate?")
    print("1. Voltage (V)")
    print("2. Current (I)")
    print("3. Resistance (R)")
    
    choice = input("Enter 1, 2, or 3: ")

    try:
        if choice == '1':

            current = float(input("Enter the current (I) in amperes: "))
            resistance = float(input("Enter the resistance (R) in ohms: "))
            voltage = calculate_voltage(current, resistance)
            print(f"Voltage (V) = {voltage:.2f} volts")
        
        elif choice == '2':

            voltage = float(input("Enter the voltage (V) in volts: "))
            resistance = float(input("Enter the resistance (R) in ohms: "))
            if resistance == 0:
                print("Resistance cannot be zero when calculating current.")
            else:
                current = calculate_current(voltage, resistance)
                print(f"Current (I) = {current:.2f} amperes")
        
        elif choice == '3':
 
            voltage = float(input("Enter the voltage (V) in volts: "))
            current = float(input("Enter the current (I) in amperes: "))
            if current == 0:
                print("Current cannot be zero when calculating resistance.")
            else:
                resistance = calculate_resistance(voltage, current)
                print(f"Resistance (R) = {resistance:.2f} ohms")
        
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
    
    except ValueError:
        print("Please enter valid numerical values.")

ohms_law_calculator()

