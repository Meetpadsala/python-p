# def greet():
#     print("Hello!")

# def wrapper():
#     print("Before greeting")
#     greet()
#     print("After greeting")

# wrapper()



def decorator_function(original_function):
    def wrapper():
        print("work")
        original_function()
        print("work Done")
    return wrapper

@decorator_function
def greet():
    print("Hello, Meet!")

greet()

