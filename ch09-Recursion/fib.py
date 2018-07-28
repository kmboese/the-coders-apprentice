import time

# Global variables
fibNumbers = [None]*1024
# a counter for how many times a memoized fibonacci number was used
memoizedRefCount = 0

# Uses recursion to return the nth number of the Fibonacci sequence. 
# Runtime grows exponentially with each recursive call.
def fib(n):
    if (n <= 2):
        return 1
    return (fib(n-1) + fib(n-2))

def fibDepth(n, depth=0):
    print("{}n={}".format(depth*4*'-', n))
    if (n <= 2):
        return 1
    depth += 1
    return(fibDepth(n-1, depth) + fibDepth(n-2, depth))

# Uses memoized recursion to return the nth number of the Fibonacci sequence in O(n) time. 
def fibMemoized(n):
    global fibNumbers
    global memoizedRefCount

    # If the nth fibonacci number has already been calculated, simply return its value
    if (fibNumbers[n]):
        memoizedRefCount += 1
        return fibNumbers[n]

    # Base case
    elif (n<=2):
        return 1

    # Otherwise, save the result of the fibonacci calculation for use later
    else:
        fibNumbers[n] = fibMemoized(n-1) + fibMemoized(n-2)

def fibDynamic(n):
    return

    

def main():
    global fibNumbers
    global memoizedRefCount


    #for i in range(1,10):
        #print("fib({}) == {}".format(i, fib(i)))

    #print(fibDepth(10))

    loops = 38
    roundingDigits = 5
    # Benchmark non-memoized function
    print("Calculating fib values using non-memoized function...")
    nonMemoizedStart = time.time()
    for i in range(1,loops):
        fib(i)
    nonMemoizedEnd = time.time()
    nonMemoizedTime = round(nonMemoizedEnd-nonMemoizedStart,roundingDigits)

    # Benchmark memoized function
    print("Calculating fib values using memoized function...")
    memoizedStart = time.time()
    for i in range(1,loops):
        fibMemoized(i)
    memoizedEnd = time.time()
    memoizedTime = round(memoizedEnd-memoizedStart,roundingDigits)

    print("Non-memoized calculation took {} seconds".format(nonMemoizedTime))
    print("Memoized calculation took {} seconds".format(memoizedTime))

if __name__ == "__main__":
    main()
