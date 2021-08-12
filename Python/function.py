# Reference : 
# https://realpython.com/defining-your-own-python-function/


print("example for the pass by assigment")
# for the argument passing in python that using in function => pass by assignment.
def f(x):
    x = 'foo'

for i in (
        40,
        dict(foo=1, bar=2),
        {1, 2, 3},
        'bar',
        ['foo', 'bar', 'baz']):
    f(i)
    print(i)


print("\n example for the reference")

# However, the following example 
# f() can use the reference to make modifications inside my_list.
def f(x):
    x['bar'] = 22


my_dict = {'foo': 1, 'bar': 2, 'baz': 3}

f(my_dict)
print(my_dict)


# Argument Tuple packing (*args)
def avg(*args):
    return sum(args) / len(args)


avg(1, 2, 3)

print("\nexample for the argument tuple unpacking")


# Argument Tuple unpacking (*)
def f(x,y,z):
   """ return the input one by one
        keyword arguments:
        x -- 
        y -- 
        z --
   """
   print(x)
   print(y)
   print(z)

a = ['foo', 'bar', 'baz']
type(a)

f(*a)

print("\nexample for the doc string")
### docstring 
print(f.__doc__)