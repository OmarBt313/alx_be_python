# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Conversion Functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main User Interaction
def main():
    try:
        # Get user input
        temp = input("Enter the temperature: ")
        if not temp.replace('.', '', 1).isdigit() and not (temp[0] == '-' and temp[1:].replace('.', '', 1).isdigit()):
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temp = float(temp)
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

        # Perform conversion
        if unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp} Fahrenheit is equal to {converted_temp:.2f} Celsius.")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp} Celsius is equal to {converted_temp:.2f} Fahrenheit.")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()