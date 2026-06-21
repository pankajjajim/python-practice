# Function to find the greatest of three numbers
a = 10
b = 20
c = 15
def greatest(a,b,c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    else:
        return c
print("Greatest of three numbers is: ", greatest(a,b,c))   

#function to find the temmperature in converting from celsius to fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

f = int(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit is: ", celsius_to_fahrenheit(f))


#Function using print pattern

def pattern(n):
    if(n == 0):
        return
    print("*" * n)
    pattern(n - 1)
pattern(3)     