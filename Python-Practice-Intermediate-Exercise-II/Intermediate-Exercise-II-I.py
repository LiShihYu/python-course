# Write a function called "factorPrime" that takes an integer as input, and returns the prime factorization of the input.
# factorPrime 質因數分解

def factorPrime(num):
    answer = str(num) + " = "  # 120 = 2 * 2 * 2 * 3 * 5

    # if n cannot be divided by 2
    # then n cannot be dived by any multiples of 2
    prime = 2

    while (prime <= num):
        if num % prime == 0:
            answer += str(prime) + " * "
            num /= prime
        else:
            prime += 1

    return answer[:len(answer) - 3]


# 利用離散數學的質因數分解
def factorPrime2(num):
    factors = {}
    divisor = 2

    while num > 1:
        count = 0
        while num % divisor == 0:
            num //= divisor
            count += 1

        if count > 0:
            factors[divisor] = count

        divisor += 1

        if divisor * divisor > num:
            break

    if num > 1:
        factors[num] = 1

    return factors


print(factorPrime2(120))
