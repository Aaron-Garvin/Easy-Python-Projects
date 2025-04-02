def convert_temperature(option, temp):
    if option == 1: return temp * 9/5 + 32, "°F"
    if option == 2: return temp + 273.15, "K"
    if option == 3: return (temp - 32) * 5/9, "°C"
    if option == 4: return (temp - 32) * 5/9 + 273.15, "K"
    if option == 5: return temp - 273.15, "°C"
    if option == 6: return (temp - 273.15) * 9/5 + 32, "°F"
    return None, "Invalid choice"
# Here the above function is used for choose the different options and the formulas respectivily
def main():
    options = ["Celsius to Fahrenheit", "Celsius to Kelvin", "Fahrenheit to Celsius", "Fahrenheit to Kelvin", "Kelvin to Celsius", "Kelvin to Fahrenheit"]
    for i, opt in enumerate(options, 1): print(i, ":", opt)
# Here enumerate() used for loop through the options list while automatically assigning an index (starting from 1)
    choice = int(input("Choose an option (1-6): "))
    temp = float(input("Enter temperature: "))
    result, unit = convert_temperature(choice, temp)
    if unit != "Invalid choice":
        print("Converted:", result, unit)
    else:
        print(unit)
main()
