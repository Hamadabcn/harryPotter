students = [
    {"name": "Hermione", "House":"Gryffindor", "Patronus": "Otter"},
    {"name": "Herry", "House":"Gryffindor", "Patronus": "Stag"},
    {"name": "Ron", "House":"Gryffindor", "Patronus": "Jack Russell Terrir"},
    {"name": "Draco", "House":"Slytherin", "Patronus": "None"},
    {"name": "Frida", "House":"Slytherin", "Patronus": "Flamingo"},
    {"name": "Yassin", "House":"Gryffindor", "Patronus": "Penguin"},
] 
for student in students:
    print (student["name"], student["House"], student["Patronus"], sep=", ")
