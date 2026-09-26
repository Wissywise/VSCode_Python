"""def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Before executing the original function.")
        result = original_function(*args, **kwargs)
        print("After executing the original function.")
        return result
    return wrapper_function """

"""def decorator_function(inner_function):
    def wrapper_function():
        print("This will be printed first.")
        inner_function()
        print("This will be printed last.")   
    return wrapper_function

def magic_print():
    print("This is MAGICAL!.")

magic = decorator_function(magic_print)
print(magic)  # Print the wrapper function
print(magic())
magic()  # Call the wrapper function
print(magic.__name__)  # Print the name of the wrapper function
print(magic.__doc__)  # Print the docstring of the wrapper function
print(magic.__module__)  # Print the module of the wrapper function
print(magic.__annotations__)  # Print the annotations of the wrapper function
print(magic.__qualname__)  # Print the qualified name of the wrapper function
print(magic.__closure__)  # Print the closure of the wrapper function
print(magic.__code__)  # Print the code object of the wrapper function
print(magic.__defaults__)  # Print the default values of the wrapper function"""



def decorator_function(inner_function):
    def wrapper_function():
        print("This will be printed first.")
        inner_function()
        print("This will be printed last.")   
    return wrapper_function

@decorator_function # This is a decorator that takes the function below it as an argument and returns the wrapper function.
def magic_print():
    print("This is MAGICAL!.")

magic = magic_print()
print(magic)

@decorator_function
def normal_print():
    print("This is a normal print statement.")

magic = normal_print()
print(magic)