
def is_prime(num):
    """
    Returns 1 if the given number is prime, 0 otherwise.
    """
    if num < 2:
        return 0
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0
    
    return 1