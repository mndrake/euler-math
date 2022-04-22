from euler_math import memoize, timer, PrimeQ, PrimePi, primes, is_prime, prime, GCD, LCM, FactorInteger, DivisorSigma
from collections import Counter


def test_euler_memoize():
    # counter for number of calls for a given fib(n)
    calls = Counter()

    # memoized fibonacci function
    @memoize
    def fib(n):
        calls[n] += 1
        if n in [1,2]:
            return 1
        else:
            return fib(n-1)+fib(n-2)

    result = fib(5)
    max_calls = max(calls.values())
    
    assert result == 5
    assert max_calls == 1
    

def test_euler_timer():
    def add_two_numbers():
        return 1+2
    timer(add_two_numbers)
    assert True
   

def test_euler_PrimeQ():
    assert PrimeQ(1033)
    assert PrimeQ(10**2000 + 4561)


def test_euler_primes():
    p = primes()
    assert next(p) == 2   
    assert next(p) == 3
    assert next(p) == 5 
    assert next(p) == 7 
    assert next(p) == 11 
    assert next(p) == 13 


def test_euler_is_prime():
    assert is_prime(1033)
    
    
def test_euler_prime():
    assert prime(173) == 1033
    
    
def test_euler_PrimePi():
    assert PrimePi(100) == 25


def test_euler_GCD():
    assert GCD(25, 80) == 5


def test_euler_LCM():
    assert LCM(25, 80) == 400


def test_euler_FactorInteger():
    assert FactorInteger(5489003) == [(13, 1), (422231, 1)]


def test_euler_DivisorSigma():    
    assert DivisorSigma(20,2) == 546
