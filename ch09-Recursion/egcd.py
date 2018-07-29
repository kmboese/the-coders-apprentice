def egcd(a, b):
    print("Entered egcd: a = {}, b = {}".format(a,b))
    if (a > b):
        greatest = a
        smallest = b
    else:
        greatest = b
        smallest = a

    modResult = greatest%smallest
    if (modResult == 0):
        return smallest
    else:
        return egcd(smallest, modResult)
