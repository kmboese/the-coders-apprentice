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

    # If the nth fibonacci number has already been calculated, simply return its value
    if (fibNumbers[n]):
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