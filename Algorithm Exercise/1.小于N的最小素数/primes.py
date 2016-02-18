primes = [2]

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

num = 100
print(num, "is a prime number:", calcPrime(num) is True)
print("小于", num, "的最小素数是", primes[len(primes) - 1])
print(primes)