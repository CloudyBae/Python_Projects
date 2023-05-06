"""Your task is to write the code that calculates the energy points that get awarded to players when they complete a level.

The points awarded depend on two things:

The level (a number) that the player completed.
The base value of each magical item collected by the player during that level.
The energy points are awarded according to the following rules:

For each magical item, take the base value and find all the multiples of that value that are less than the level number.
Combine the sets of numbers.
Remove any duplicates.
Calculate the sum of all the numbers that are left."""

def sum_of_multiples(limit, multiples):
    numbers = []
    if len(multiples) >= 1 and multiples[0] != 0:
        for i in range(len(multiples)):
            if multiples[i] == 0:
                pass
            else: 
                for nums in range(0, limit, multiples[i]):
                    numbers.append(nums)
       
    set_numbers = set(numbers)
    return sum(set_numbers)

