import random
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# in Python, the @classmethod decorator is used to declare a method in the class as a class method 
# that can be called using ClassName. MethodName(). The class method can also be called using an 
# object of the class. The @classmethod is an alternative of the classmethod() function. 
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
Hat.sort("Harry")  
