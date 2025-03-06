import time
# *args, **kwargs are used in the case of multiple arguments passed
# timer calculate the time elapsed during the func excecution
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('func takes', end - start, 'seconds')

    return wrapper

@timer
def func1(x,y):
    z = x + y

func1(4,5)

