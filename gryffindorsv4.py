# Dictionary comprehension is a method for transforming one dictionary into another dictionary
students = ["Hermione", "Harry", "Ron", "Padma", "Frida"]

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)