# Write a function called "isPrime" that takes an integer as input, and returns a boolean value that indicates if the input number is prime.
# prime 質數

def isPrime(num):
    if num == 1:

        print("False")
        return False

    # test if 2, 3, 4, 5, ..., n - 1 can divide num
    starter = 2
    while starter < num:
        if num % starter == 0:
            print("False")
            return False
        starter += 1

    print("True")
    return True


def isPrime2(num):
    if num == 1:
        return False

    # test if 2, 3, 4, 5, ..., n - 1 can divide num
    starter = 2
    for starter in range(2, num):
        if num % starter == 0:
            return False
    return True


print(isPrime2(1))
print(isPrime2(5))
print(isPrime2(91))
print(isPrime2(1000000))
print(isPrime2(10001))
