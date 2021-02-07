def celsius_to_fahrenheit(temp_in_celsius):
    if isinstance(temp_in_celsius, int):
        temp_in_fahrenheit = temp_in_celsius * 1.8 + 32
        return temp_in_fahrenheit

def fahrenheit_to_celsius(temp_in_fahrenheit):
    if isinstance(temp_in_fahrenheit, int):
        temp_in_celsius = (temp_in_fahrenheit - 32) / 1.8
        return temp_in_celsius