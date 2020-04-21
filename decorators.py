# Decorator takes a function as an input return a new function- functional programming  

def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function.")
    return wrapper

def hello():
    print("Hwllo, world!")