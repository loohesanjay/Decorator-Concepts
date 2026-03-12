import time
import functools

def execution_timer(func):
    """1. Execution time checker decorator."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        log = f"Task: {func.__name__} | Time: {end-start:.4f}s\n"
        with open("decorator_output.txt", "a") as f:
            f.write(log)
        return result
    return wrapper

def call_counter(func):
    """3. Function call counter decorator."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        log = f"Task: {func.__name__} | Call Count: {wrapper.count}\n"
        with open("decorator_output.txt", "a") as f:
            f.write(log)
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@execution_timer
@call_counter
def process_data():
    time.sleep(0.5) 
    return "Data Processed"

if __name__ == "__main__":
    
    open("decorator_output.txt", "w").close()
    process_data()
    process_data()
    print("Decorators executed! Check decorator_output.txt")