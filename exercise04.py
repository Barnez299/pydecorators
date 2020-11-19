# converting a function decorator into a Class decorator
from decorator_template import CountCalls, count_calls

@CountCalls
def fibonacci(number):
    """Calculate Fibonacci numbers fib_n
    The Fibonacci numbers are 1, 2, 3, 5, 8, 13, 21, ...
      fib_n = fib_n-1 + fib_n-2
    """
    if number < 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci.num_calls)
print(fibonacci(7))
print(fibonacci.num_calls)
print(fibonacci(32))
print(fibonacci.num_calls)

