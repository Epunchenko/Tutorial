
#2
"""
def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"
"""

#3
"""
base_rate = 40
price_per_km = 10
total_trip = 0


def calculate_trip_price(distance_km):
    global total_trip
    total_trip += 1
    return base_rate + price_per_km * distance_km
    

calculate_trip_price(10)
print(total_trip)
print(calculate_trip_price(10))
"""

#4
"""
def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price - price * discount        

    apply_discount()
    return price
print(discount_price(100, 0.1))
"""

#5
"""
def get_fullname(first_name, last_name, middle_name = None):
    if middle_name == None:
        return f"{first_name} {last_name}"
    else:
        return f"{first_name} {middle_name} {last_name}"

print(get_fullname("Jack", "Anna", "Bob"))
"""

#6
"""
def format_string(string, length, space = " "):
    if len(string) >= length:
        return string
    else:
        return ((length - len(string)) // 2) * space + string
print(format_string(string='aaaaaaaaaaaaaaaaac', length=12))
print(format_string(length=15, string='abaa'))
"""

#7

"""
def first(size, *topics):
    return size + len(topics)


first(5, "first", "second", "third")
first(1, "Alex", "Boris")


def second(size, **comments):
    return size + len(comments)


second(3, comment_one="first", comment_two="second", comment_third="third")
second(10, comment_one="Alex", comment_two="Boris"
"""

#8
"""
def cost_delivery(quantity, *_, discount = 0):
    result = 0
    if quantity > 1:
        result = (quantity - 1) * 2 + 5
    else:
        result = quantity * 5
    result = result - result * discount
    return result


print(cost_delivery(2, 1, 2, 3))
print(cost_delivery(3, 3))
print(cost_delivery(1))
print(cost_delivery(2, 1, 2, 3, discount=0.5))
"""

#9

# def cost_delivery(quantity, *_, discount=0):
#    """Функція повертає суму за доставлення замовлення.

#    Перший параметр quantity - кількість товарів в замовленні.    
#    Параметр знижки discount, який передається лише як ключовий, за 
#    замовчуванням має значення 0."""
#    result = (5 + 2 * (quantity - 1)) * (1 - discount)
#    return result


# print(cost_delivery.__doc__)

#10
"""
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
        
def number_of_groups(n, k):
    C = factorial(n) / (factorial(n-k) * factorial(k))
    return int(C)
print(number_of_groups(50, 7))
"""

#11
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(3))
"""