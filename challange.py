import time

current_time = time.time()


def speed_calc_decorator(function):
    def wrapper_function():
        first_run = time.time()
        function()
        seccond_run = time.time()
        print(f"{function.__name__} run speed: {seccond_run - first_run}")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
