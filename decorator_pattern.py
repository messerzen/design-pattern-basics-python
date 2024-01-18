from functools import wraps

def make_blink(function):

    """Defines the decorator"""

    #This mnakes the decorator transparent in terms of its name and docs
    @wraps(function)

    def decorator():
        # Grab the return value of the funcion beign decorated
        ret = function()

        #Add new functionality to the function beign decorated
        return "<blink>" + ret + "/blink>"
    
    return decorator

# We apply the decorator here

def hello_world():
    "Original function"

    return "Hello, world!"

@make_blink
def hello_world2():
    "Original function"

    return "Hello, world!"
if __name__ == "__main__":

    print(hello_world())
    print(hello_world2())