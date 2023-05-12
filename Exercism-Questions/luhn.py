"""Instructions
Given a number determine whether or not it is valid per the Luhn formula.
The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers and Canadian Social Insurance Numbers.
The task is to check if a given string is valid.
Validating a Number
Strings of length 1 or less are not valid. Spaces are allowed in the input, but they should be stripped before checking. All other non-digit characters are disallowed."""
class Luhn:
    def __init__(self, card_num):
        self._card_num = card_num

    def valid(self):
        # removes spaces
        card = self._card_num.replace(" ", "")
        
        # length 1 or less & not all numbers returns a False validity value
        if (len(card) <= 1) or (not card.isdigit()):
            return False
        
        # revereses the list and doubles every other digit
        number = [int(i) for i in card[::-1]]
        for num in range(1, len(number), 2):
            number[num] *= 2
            if number[num] > 9:
                number[num] -= 9
        
        # sums digits & checks if it is evenly divisible by 10
        return sum(number) % 10 == 0