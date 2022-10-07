#https://realpython.com/python-namespaces-scope/

print(dir(__builtins__))


print("This is my file to test Python's execution methods.")
print("The variable __name__ tells me which context this file is running in.")
print("The value of __name__ is:", repr(__name__))



# https://realpython.com/python-scope-legb-rule/


import sys 
print( sys.__dict__.keys() ) 


import helpers
# a good way to check what is in the namepsace
print(helpers.__dict__.keys())


# Python resolves names using the so-called LEGB rule
# 

### Example 1 
print("Example 1")
x = 'global'

def f():

    def g():
        print(x)

    g()


f()


### Example 2
print("Example 2")
x = 10
print(globals())
