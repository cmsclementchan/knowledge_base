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
  return x+5

result = add5(3)
print(result)



