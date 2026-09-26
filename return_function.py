def outer_function( which_function):
    print("This is the outer function.")
    def first_inner_function():
        print("This is the first inner function.")

    def second_inner_function():
        print("This is the second inner function.")

    if which_function == "first":
        return first_inner_function

    if which_function == "second":
        return second_inner_function

x = outer_function("first")  # Call the outer function and get the first inner function
print(x)  # Print the first inner function
x()  # Call the first inner function
    
    