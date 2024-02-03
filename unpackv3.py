# *args specifies the number of non-keyword arguments that can be passed and the operations that can be 
# performed on the function in Python whereas 
# **kwargs is a variable number of keyword arguments that can be passed to a function that can perform
# dictionary operations
def f(*args, **kwargs):
    print("Named:", kwargs) 
    
f(galleons=100, sickles=50, knuts=25 )