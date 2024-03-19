#My First Python App

print("Select an option: ")
print("1. Convert to Celcius")
print("2. Convert to Fahrenheit")
print("0. Exit")


def toCelcius(fahrenheit):
    celcius = (fahrenheit-32) * 5/9
    return celcius

def toFahrenheit(celcius):
    fahrenheit = (celcius * 1.8)+32
    return fahrenheit

inp = int(input())

while(inp >2):
    print("Wrong option. Please try again: ")
    inp = int(input())

if inp == 1:
    print("Fahrenheit: ")
    fahr = float(input())
    print(toCelcius(fahr))
elif inp == 2:
    print("Celcius: ")
    celc = float(input())
    print(toFahrenheit(celc))
elif inp == 0:
    exit()
    
    
