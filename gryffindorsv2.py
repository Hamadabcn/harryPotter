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
def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])