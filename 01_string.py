name = input("Enter your name: ")
print(f"Good Afternoon {name}") #f-string is used to format the string and print the output.

#problem statement: replace the name and date
letter = '''Dear <|NAME|>,
you are selected!
Date: <|DATE|>'''
print(letter.replace("<|NAME|>", name).replace("<|DATE|>", "2023-10-10"))

#Find the double spaces
name = "Pankaj  Jajim is a data scientist and a  machine learning engineer"
print(name.find("  "))
print(name.replace("  ", " "))
print(name) #The original string is not changed because strings are immutable in Python. The replace() function returns a new string with the replacements, but it does not modify the original string.