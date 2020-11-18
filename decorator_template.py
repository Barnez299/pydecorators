# this is a basic structure for a decorator function
import functools
import time


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


def trace(func):
    """Trace decorator """

    @functools.wraps(func)
    def _trace(*args, **kwargs):
        """The timer function replacing the original"""
        # do something before
        value = func(*args, **kwargs)
        # do something after
        print(f'this is printing')
        return value

    return _trace