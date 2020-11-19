import random
from decorator_template import trace, timer


GREETINGS = ["Heisann", "Hi there", "Ni!"]

@timer
@trace
def greet(name, greeting="Hello"):
    return f"{greeting} {name}"

@timer
@trace
def random_greet(name="Emily"):
    greeting = random.choice(GREETINGS)
    return greet(name, greeting=greeting)

@timer
@trace
def greet_many(number):
    return [random_greet() for _ in range(number)]


random.seed(2020)
greet('world')
print('-' * 50)
greet(name='world', greeting='def')
print('-' * 50)
random_greet()
print('-' * 50)
greet_many(3)
