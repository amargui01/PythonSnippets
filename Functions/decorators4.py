def price_string(func):
    def wrapper(quantity):
        return "£" + str(func(quantity))

    return wrapper
@price_string
def new_price(price):
    return (float(price * 0.9))

price = new_price(100)
print(price)