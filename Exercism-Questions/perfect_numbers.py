"""Determine if a number is perfect, abundant, or deficient based on Nicomachus' (60 - 120 CE) classification scheme for positive integers.

The Greek mathematician Nicomachus devised a classification scheme for positive integers, identifying each as belonging uniquely to the categories of perfect, 
abundant, or deficient based on their aliquot sum. The aliquot sum is defined as the sum of the factors of a number not including the number itself. 
For example, the aliquot sum of 15 is (1 + 3 + 5) = 9"""

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    numbers = 0
    for i in range(1, number):
        if number % i == 0: numbers += i
    
    if numbers == number: 
        return "perfect"
    if numbers > number: 
        return "abundant" 
    return "deficient"