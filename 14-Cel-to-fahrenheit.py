def cel_to_fahren(c):
    return (c*9/5)+32


Celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = cel_to_fahren(Celsius)


print(f"{Celsius} C is equal to {fahrenheit} F")