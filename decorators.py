# Decorator takes a function as an input return a new function- functional programming  
#Wrapper function

def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hala, world!")

hello()