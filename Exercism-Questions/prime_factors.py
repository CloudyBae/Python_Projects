"""Compute the prime factors of a given natural number.
A prime number is only evenly divisible by itself and 1.
Note that 1 is not a prime number."""

def factors(value):
    numbers = []
    num = 2
    
    while value > 1:
        while value % num == 0:
            value = value / num
            numbers.append(num)
        num += 1
                   
    return numbers        


result = factors(93819012551)
print(result)