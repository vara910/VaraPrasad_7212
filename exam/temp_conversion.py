# Temperature Conversion Tool
# - Write a program that converts temperatures between Celsius, Fahrenheit, and Kelvin
# based on user input.
# - Use functions for each conversion.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def main():
    conversions = {
        1: ("Celsius", "Fahrenheit", celsius_to_fahrenheit),
        2: ("Fahrenheit", "Celsius", fahrenheit_to_celsius),
        3: ("Celsius", "Kelvin", celsius_to_kelvin),
        4: ("Kelvin", "Celsius", kelvin_to_celsius)
    }
    
    print("Temperature Conversion Tool")
    for key, (from_unit, to_unit, _) in conversions.items():
        print(f"{key}. {from_unit} to {to_unit}")
    
    choice = int(input("Choose a conversion (1-4): "))
    if choice in conversions:
        from_unit, to_unit, conversion_func = conversions[choice]
        temp = float(input(f"Enter the temperature in {from_unit}: "))
        converted_temp = conversion_func(temp)
        print(f"{temp} {from_unit} is {converted_temp} {to_unit}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
