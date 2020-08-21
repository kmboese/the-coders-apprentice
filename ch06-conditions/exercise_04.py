import math

def main():
    # Quadratic equation: Ax^2 + Bx + C = 0
    # Solutions: (-B +- sqrt(B^2 - 4AC))/(2A)
    
    print('Enter values for the quadratic equation: Ax^2 + Bx + C = 0')
    A = float(input('Enter a value for A: '))
    B = float(input('Enter a value for B: '))
    C = float(input('Enter a value for C: '))
    print('Solving the equation {}x^2 + {}x + {} = 0'.format(A, B, C))

    # Calculate the discriminant
    discriminant = math.pow(B,2) - 4*A*C

    # Case 1: No solutions if root is negative
    if discriminant < 0.0:
        print('There are no solutions to the equation')
        exit()
    elif discriminant == 0.0:
        print('There is one solution: {}'.format(-1*B/2*A))
        exit()
    
    # Calculate the root if positive
    root = math.sqrt(discriminant)

    # Special cases: A is zero and both A and B are zero
    if A == 0:
        if B == 0:
            print('There are no solutions to the equation')
        else:
            print('There is one solution: x = {}'.format(-1*C/B))
    
    # Standard case: two solutions
    print('Solution 1: {}'.format( (-1*B + root)/(2*A)))
    print('Solution 2: {}'.format((-1*B - root)/(2*A)))
    
    

if __name__ == '__main__':
    main()