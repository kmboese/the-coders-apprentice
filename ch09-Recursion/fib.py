import time

# Global variables
fibNumbers = [None]*1000000
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
def fibMemoizedTopDown(n):
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
        fibNumbers[n] = fibMemoizedTopDown(n-1) + fibMemoizedTopDown(n-2)
        return fibNumbers[n]

def fibMemoizedBottomUp(n, fibArray=[None]*100000):
    if fibArray[n]:
        return fibArray[n]
    elif (n<=2):
        return 1
    i = 3
    while i <= n:
        fibArray[0] = 1
        fibArray[1] = 1
        fibArray[i-1] = fibMemoizedBottomUp(i-2, fibArray) + fibMemoizedBottomUp(i-3, fibArray)
        i += 1
    return fibArray[n-1]


    

def main():
    global fibNumbers
    global memoizedRefCount


    #for i in range(1,10):
        #print("fib({}) == {}".format(i, fib(i)))

    #print(fibDepth(10))

    loops = 10000
    roundingDigits = 5

    for i in range(1,11):
        #print("fib({}) = {}, fibMemoizedBottomUp({}) = {}, fibMemozedTopDown({}) = {}"\
            #.format(i, fib(i), i, fibMemoizedBottomUp(i), i, fibMemoizedTopDown(i)))
        assert(fib(i) == fibMemoizedBottomUp(i))
        assert(fib(i) == fibMemoizedTopDown(i))

    '''
    # Benchmark non-memoized function
    print("Calculating fib values using non-memoized function...")
    nonMemoizedStart = time.time()
    for i in range(1,loops):
        fib(i)
    nonMemoizedEnd = time.time()
    nonMemoizedTime = round(nonMemoizedEnd-nonMemoizedStart,roundingDigits)
    print("Non-memoized calculation took {} seconds".format(nonMemoizedTime))
    '''

    # Benchmark top-down function
    print("Calculating fib values using top-down memoized function...")
    topDownStart = time.time()
    for i in range(1,loops):
        fibMemoizedTopDown(i)
    topDownEnd = time.time()
    topDownTime = round(topDownEnd-topDownStart,roundingDigits)
    print("Top-down memoized calculation took {} seconds".format(topDownTime))

    # Benchmark bottom-up function
    print("Calculating fib values using bottom-up memoized function...")
    bottomUpStart = time.time()
    for i in range(1,loops):
        fibMemoizedTopDown(i)
    bottomUpEnd = time.time()
    bottomUpTime = round(bottomUpEnd-bottomUpStart,roundingDigits)
    print("Bottom-up memoized calculation took {} seconds".format(bottomUpTime))

if __name__ == "__main__":
    main()
