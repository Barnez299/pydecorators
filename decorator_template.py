# this is a basic structure for a decorator function
import functools
import time

REGISTERED = {}


def register(func):
    """Register a function"""
    REGISTERED[func.__name__] = func
    return func


def timer(func):
    """Timing how long function takes to run"""

    @functools.wraps(func)
    def _timer(*args, **kwargs):
        """The timer function replacing the original"""
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        print(f'Elapsed time: {toc - tic:.2f} seconds')
        return value

    return _timer


# tracer decorator

def trace(func):
    """Trace decorator """
    name = func.__name__


    @functools.wraps(func)
    def _trace(*args, **kwargs):
        """The timer function replacing the original"""
        # do something before
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ','.join(args_repr + kwargs_repr)
        print(f"Calling {name} ({signature})")
        value = func(*args, **kwargs)
        # do something after
        print(f"Calling {name} returned {value !r}")
        return value

    return _trace


# converting a function decorator into a Class decorator

def count_calls(func):

    """Count the number of calls to a function"""

    @functools.wraps(func)
    def _count_calls(*args, **kwargs):
        _count_calls.num_calls += 1
        return func(*args, **kwargs)

    _count_calls.num_calls = 0
    return _count_calls


class CountCalls:
    
    """Count the number of calls to a function"""

    def __init__(self, func):
        
        self.func = func
        self.num_calls = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        return self.func(*args, **kwargs)