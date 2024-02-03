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
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print("Gryffindor")