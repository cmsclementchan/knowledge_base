class ExampleClass(object):
    class_attr = 0
    def __init__(self, instance_attr):
        self.instance_attr = instance_attr



if __name__ == '__main__' :
    foo = ExampleClass(1)
    bar = ExampleClass(2)
    print(ExampleClass.__dict__)
    #{'__module__': '__main__', 'class_attr': 0, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None, '__init__': <function __init__ at 0x031192F0>}
    print(foo.__dict__)
    #{'instance_attr': 1}
    print(bar.__dict__)
    #{'instance_attr': 2}
    print(bar.__class__.__dict__)

# reference : 
# https://dzone.com/articles/python-class-attributes-vs-instance-attributes#:~:text=A%20class%20attribute%20is%20a,.)%20%2C%20of%20the%20class.
