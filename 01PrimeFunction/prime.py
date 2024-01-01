import pyprime
import numpy as np
from multiprocessing import Pool
import pickle
import math
import sys

execution_times = {}
functions_executed = set()
speedups = []

results = {}


def timeit(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        execution_times[func.__name__] = end - start
        results[func.__name__] = result
        if func.__name__ == 'cprimes':
            print(f"C++: {execution_times['cprimes']}s", end=", ")
            sys.stdout.flush()
        functions_executed.add(func.__name__)
        if len(functions_executed) == 2:
            print_speedup()
            functions_executed.clear()
        return result
    return wrapper


lengths = []  # Define lengths as a global variable


def print_speedup():
    if 'cprimes' in execution_times and 'pyprimes' in execution_times:
        # Load the prime numbers from the pickle file
        with open('primes.pkl', 'rb') as f:
            pyprimes_list = pickle.load(f)

        # Load the prime numbers from the txt file
        with open('primes.txt', 'r') as f:
            cprimes_list = [int(line.strip()) for line in f]

        # Convert the lists to sets and compare
        if set(cprimes_list) == set(pyprimes_list):
            speedup = execution_times['pyprimes'] / execution_times['cprimes']
            print(
                f"Python: {execution_times['pyprimes']}s, Speedup: {speedup}\n")
            speedups.append(speedup)  # Always append speedup to the list
        else:
            print("Results are not equal, no speedup calculated\n")
    else:
        print("'cprimes' and/or 'pyprimes' not in execution_times")


@timeit
def cprimes(n):
    lst = pyprime.primes(n)
    return lst


@timeit
def pyprimes(n):
    prime = np.ones(n // 2, dtype=bool)
    limit = int(n**0.5) + 1
    for p in range(3, limit, 2):
        if prime[p // 2]:
            prime[p*p // 2::p] = 0

    primes = np.r_[2, 2*np.nonzero(prime)[0][1::]+1].tolist()

    with open('primes.pkl', 'wb') as f:
        pickle.dump(primes, f)
    return primes
