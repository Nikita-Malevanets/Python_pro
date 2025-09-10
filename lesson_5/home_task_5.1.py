def analyze_object(obj):
    print(type(obj))

    for name, value in obj.__dict__.items():
        print(f'{name} : {type(value)}')

    for name in dir(type(obj)):
        if name.startswith('__'):
            attr = getattr(obj, name)
            if callable(attr):
                print(f'{name} : {type(attr)}')


class MyClass:
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        return f"Hello, {self.value}"


obj = MyClass("World")
analyze_object(obj)
