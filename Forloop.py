#Print multiplication table using for loop
n = int(input("enter number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")


#Print person name starting with letter 'P' from a list of names 
l = ["Pankaj", "Ramesh", "Pooja", "Suresh", "Priya"]

for name in l:
    if (name.startswith("P")):
        print(f"Hello {name}")

#Print the prime numbers
n = int(input("enter number: "))   

for i in range(2,n):
    if(n%i) == 0:
        print("number in not prime")
        break
else:
    print("number is prime")
        
        
#Print factorial of a number
n = int(input("enter number: "))

product = 1
for i in range(1, n+1):
    product = product * i
print(f"Factorial of {n} is {product}")

#Print mutliplication table of a number in reverse order
n = int(input("enter number: "))

for i in range(1, 11):
    print(f"{n} x {11-i} = {n*(11-i)}")
