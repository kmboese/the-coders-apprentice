from fib import fib, fibMemoizedBottomUp, fibMemoizedTopDown
import time

def main():
    global fibNumbers
    global memoizedRefCount


    #for i in range(1,10):
        #print("fib({}) == {}".format(i, fib(i)))

    #print(fibDepth(10))

    loops = 50000
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
