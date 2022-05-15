from random import choices


def fruit():
    fruits = ["apple", "cherry", "banana", "pear"]
    return choices(fruits)[0]

def meal(beverage):
    my_fruit = fruit()
    print(f"your fruit is {my_fruit} and your beverage is {beverage}")
    if my_fruit == "cherry":
        return f"Your meal is a {my_fruit} and {beverage}"
    return f"Your meal is a steak and {beverage}"


# var = 1
# var = var
