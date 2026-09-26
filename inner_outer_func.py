## inner functions
def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")
    
    print("This is other outer function.")

    #inner_function()  # Call the inner function
    return inner_function  # Return the inner function without calling it

#outer_function()  # Call the outer function

## calling the inner function returned by the outer function
#outer_func = outer_function()  # Call the outer function and get the inner function
#print(outer_func)  # Print the inner function memory address
#outer_func()  # Call the inner function
#print(outer_func())  # Call the inner function and print the return value (None)

## decorators
def decorator_function(inner_function):
    def wrapper_function():
        print("I am the wrapper function.")

        inner_function()
        print("I am the inner function.")   

    return wrapper_function # Return the wrapper function without calling it

def modified_function():
    print("I am the modified function.")

z = decorator_function(modified_function)  # Call the decorator function and get the wrapper function
#print(z)  # Print the wrapper function memory address
#z()  # Call the wrapper function


## @decorator_function
@decorator_function #
def modified_function():
    print("I am the modified function.") 

x = modified_function()  # Call the modified function and get the wrapper function
print(x)  # Print the wrapper function memory address