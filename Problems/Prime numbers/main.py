prime_numbers = []
for possible_prime in range(2, 1001):
    is_prime = True
    for i in range(2, possible_prime):
        if possible_prime % i == 0:
            is_prime = False
    if is_prime:
        prime_numbers.append(possible_prime)
