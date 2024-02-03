people = [
    {"name": "Frida", "house": "Gryffindor"},
    {"name": "Yassin", "house": "Ravenclaw"},
    {"name": "Amira", "house": "Slytherin"},
    {"name": "Hamada", "house": "Hufflepuff"},
    {"name": "Tom", "house": "Slytherin"},
    {"name": "Marc", "house": "Gryffindor"},
]

# lambda function is a small anonymous function. Can take any number of arguments, but can only have one expression
people.sort(key=lambda person: person ["name"])
print(people)
