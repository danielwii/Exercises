import time


def execTime(func):
    def newFunc(*args, **args2):
        t0 = time.time()
        print("@%s, {%s} start" % (time.strftime("%X", time.localtime()), func.__name__))
        back = func(*args, **args2)
        print("@%s, {%s} end" % (time.strftime("%X", time.localtime()), func.__name__))
        print("@%.3fs taken for {%s}" % (time.time() - t0, func.__name__))
        return back

    return newFunc


primes = [2]


@execTime
def calcPrime(num):
    for n in range(3, num + 1):
        if isPrime(n):
            primes.append(n)
            if n is num: return True


def isPrime(num):
    for p in primes:
        if num % p is 0:
            return False
    return True


num = 100000
print(num, "is a prime number:", calcPrime(num) is True)
print("小于", num, "的最小素数是", primes[len(primes) - 1])
print(primes)
