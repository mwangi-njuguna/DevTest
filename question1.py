#my function to check if number is prime or not
def isPrime(num):
    try:
        return num is not None and isinstance(num, int) and num >= 2 and all([num % i != 0 for i in range(2, 1+int(num**.5))])
    except TypeError:
        return "Input not allowed!"
    

#my memoize class which memoizes the input
class Memoize:
    def __init__(self, fn):
        self.memoize = {}
        self.fn = fn

    def __call__(self, *args):
        if args not in self.memoize:
            self.memoize[args] = self.fn(*args)
        return self.memoize[args]

#memoize isPrime function
isPrime = Memoize(isPrime)


if __name__ == "__main__":
    print(isPrime(100000000000))