students = [
    {"name": "Hermoine", "house": "Gryffindor"}, 
    {"name": "Harry", "house": "Gryffindor"}, 
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
    {"name": "Yassin", "house": "Hufflepuff"},
    {"name": "Frida", "house": "Gryffindor"},
    {"name": "Amira", "house": "Slytherin"},
    {"name": "Hamada", "house": "Bensi"}
]

# The set() function creates a set object
houses = set()
for student in students:
    houses.add(student["house"])
        
for house in sorted (houses):
    print(house)
    