# def speed_calc_decorator(function):
#     def wrapper_function():
#         first_run = time.time()
#         function()
#         seccond_run = time.time()
#         print(f"{function.__name__} run speed: {seccond_run - first_run}")
#         return wrapper_function
def out_fun(function):
    def wrapper_fun(*args):
        s = function(args[0], args[1], args[2])
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {s}")
    return wrapper_fun


@out_fun
def a_function(a, b, c):
    return a * b * c


a_function(1, 2, 3)
