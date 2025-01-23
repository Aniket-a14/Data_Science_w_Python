#nested func
def outer_func(message):
    def inner_func():
        print(f"Message from inner function: {message}")
    inner_func()

outer_func("HI, hello")