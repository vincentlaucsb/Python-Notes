# Calculate n choose r
def combination(n, r):
    return factorial(n)/(factorial(r) * factorial(n - r))

# Calculate n permute r
def permutation(n, r):
    return factorial(n)/factorial(n - r)

# Calculate n!
def factorial(n):
    if (n == 0):
        return 1
    
    return n * factorial(n - 1)