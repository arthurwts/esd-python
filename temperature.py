def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Exemples d'utilisation
temp_celsius = int(input("Saisissez un nombre en degrés : "))
temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
print(temp_celsius, "degrés Celsius équivalent à", temp_fahrenheit, "degrés Fahrenheit.")

temp_fahrenheit = int(input("Saisissez un nombre en farenheit : "))
temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
print(temp_fahrenheit, "degrés Fahrenheit équivalent à", temp_celsius, "degrés Celsius.")
