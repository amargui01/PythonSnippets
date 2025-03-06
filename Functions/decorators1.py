def decorator_func(original_func):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_func.__name__}')
        return original_func(*args, **kwargs)
    return wrapper_function

@decorator_func
def display():
    print('display function ran')


@decorator_func
def display_info(name, age):
    print(f'display_info ran with arguments ({name},{age})')

display()
display_info('joe',40)
