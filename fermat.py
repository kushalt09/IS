import random

def fermat_primality_test(n, k=5):
    if n <= 1:
        return False
    if n == 2:
        return True

    for _ in range(k):

        a = random.randint(2, n-2)
 
        if pow(a, n-1, n) != 1:
            return False

    return True

number_1 = 21
number_2 = 5

is_prime_21 = fermat_primality_test(number_1)
is_prime_5 = fermat_primality_test(number_2)

print(f"Is 21 prime? {'Yes' if is_prime_21 else 'No'}")
print(f"Is 5 prime? {'Yes' if is_prime_5 else 'No'}")
