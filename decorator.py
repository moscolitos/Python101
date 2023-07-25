import time
import timeit

# Timing Decorator
def timing_decorator(func=None, show_output=True):
    if func is None:  # The decorator is used without parameters
        return lambda f: timing_decorator(f, show_output=show_output)

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        if show_output:
            arg_str = ', '.join([repr(arg) for arg in args] + [f"{key}={val!r}" for key, val in kwargs.items()])
            print(f"Execution time of {func.__name__}({arg_str}): {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Example functions to be used with the timing decorator
@timing_decorator
def slow_function():
    time.sleep(2)
    print("Slow function executed.")

@timing_decorator
def fast_function():
    print("Fast function executed.")

# Examples of Using the Decorator
@timing_decorator
def add_numbers(a, b):
    return a + b

@timing_decorator(show_output=False)
def multiply_numbers(a, b):
    return a * b

# Alternative Approach using timeit
def timeit_example():
    setup_code = "from math import sqrt"
    test_code = "sqrt(25)"
    execution_time = timeit.timeit(test_code, setup=setup_code, number=1000000)
    print(f"Execution time using timeit: {execution_time:.6f} seconds")

if __name__ == "__main__":
    # Using the timing decorator with example functions
    slow_function()
    fast_function()
    add_numbers(10, 20) 
    multiply_numbers(5, 6)

    # Using the timeit_example function
    timeit_example()
