# Self-test tasks for module 4

#1
"""
def amount_payment(payment):
    data = list(payment)
    sum = 0
    for value in data:
        if value >= 0:
            sum = sum + value
    return sum
"""

#2
"""
def prepare_data(data):
    new_data = sorted(data)
    new_data.pop(0)
    new_data.pop()
    return new_data
    """

#3
"""
def format_ingredients(items):
    items = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
    last = items.pop()
    recipe = ""
    for ingredients in items:
        recipe += ingredients + ", "
    return recipe + "and " + last


def format_ingredients(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 0:
        return ""
    else:
        return ", ".join(items[:-1]) + " and " + items[-1]

print(format_ingredients(["2 eggs"]))
"""


