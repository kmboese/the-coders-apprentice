from egcd import egcd

def main():
    a,b = 3,6
    print("GCD of {} and {} is {}".format(a, b, egcd(a,b)))

    c,d = 14,21
    print("GCD of {} and {} is {}".format(c, d, egcd(c,d)))

    e,f = 1301081, 1299721
    print("GCD of {} and {} is {}".format(e, f, egcd(e,f)))

if __name__ == "__main__":
    main()