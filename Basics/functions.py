# Functions blocks begin def followed by the function name and parentheses ().
# There are input parameters or arguments that should be placed within these parentheses.
# You can also define parameters inside these parentheses.
# There is a body within every function that starts with a colon (:) and is indented.
# You can also place documentation before the body.
# The statement return exits a function, optionally passing back a value.

def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)

add(1) # calling the function