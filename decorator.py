
def custom_fench(fench: str = "+"):
    def add_fench(func):
        def new_func(text: str):
            print(fench * len(text))
            func(text)
            print(fench * len(text))
        return  new_func
    return add_fench



# def decorator(func):
#     def new_func():
#         print("Decorator")
#         func()
#         print("Decorator")
#     return new_func
#
#
# @decorator
@custom_fench()
def log():
    print("Subrata")
