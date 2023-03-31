import sys

variable=sys.argv

def funcion(*args):
    for i in args:
        print(i)
    
funcion(variable)