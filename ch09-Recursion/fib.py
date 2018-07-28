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

def main():
    print("Starting main")
    for i in range(1,10):
        print("fib({}) == {}".format(i, fib(i)))
    print(fibDepth(10))

if __name__ == "__main__":
    main()
