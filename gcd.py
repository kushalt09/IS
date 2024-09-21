def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Test the GCD function with the numbers 31 and 2
result = gcd(31, 2)
print(f"The GCD of 31 and 2 is: {result}")
