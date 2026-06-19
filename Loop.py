#While loop
count = 1

while(count <= 5):
    print("hello world", count)
    count += 1
print("after loop, count =", count)

# print multiplication table of a number using while loop
n = int(input("enter number: "))

i = 1
while(i <= 10):
    print(n*i)    
    i += 1

# Break statement
i = 1
while(i <= 10):
    if(i % 6 == 0):
        break
    print(i)
    i += 1   

#Continue statement
i = 1
while(i <= 10):
    if(i % 3 == 0):
        i += 1
        continue
    print(i)
    i += 1

#print sum of n natural numbers using while loop
n = int(input("enter number: "))    

sum = 0
i = 1
while(i <= n):
    sum +=i
    i += 1
print(sum)    
