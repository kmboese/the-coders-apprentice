# Given an integer n, return all prime numbers k <= n. Use the 
# Sieve of Eratosthenes method to find the primes.
def sieve(n):
    # Generate the array of n numbers
    numbers = [i for i in range(0,n+1)]
    primes = []
    # Keep track of the number multiple to remove from the array
    index = 2
    while index <= n:
        key = index
        while key+index <= n:
            numbers[key+index] = None
            key += index
        index += 1
    # All the numbers left in the array are now prime
    primes = [num for num in numbers[2:] if num]
    return primes
    
