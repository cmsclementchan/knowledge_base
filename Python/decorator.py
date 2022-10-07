import functools

def my_decorator(func):

  @functools.wraps(func)
  def wrapper(*args, **kargs):
    print('Start')
    # Do...
    result = func(*args, **kargs)
    # Do...
    print('End')
    return result
  return wrapper

@my_decorator
def add5(x):
  print("in the add5 function")
  return x+5

result = add5(3)
print(result)


# Reference 
https://www.geeksforgeeks.org/function-wrappers-in-python/#:~:text=Wrappers%20around%20the%20functions%20are,function%2C%20without%20permanently%20modifying%20it.
