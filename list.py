name = ['Pankaj', 'Jajim', 4, 5.6, True, 'Mohit', 'Rakesh']
print(name)

#List slicing
print(name[0:3:1])

# List modify
name[1] = 'Saini'
print(name)

# List methods
name.append('Rohit')
name.insert(2, 'Kumar')
value = name.pop(3)
print(name)
print(value)

# Loop in list
fruits = []
for fruit in range(7):
    fruit = input(f"Enter fruit name {fruit+1}: ")
    fruits.append(fruit)
print(fruits)

#using loop to print student marks in list
marks = []
for mark in range(6):
    mark = int(input(f"Enter mark {mark+1}: "))
    marks.append(mark)
    marks.sort()
print(marks)