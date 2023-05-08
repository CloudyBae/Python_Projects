"""Instructions
Given a number from 0 to 999,999,999,999, spell out that number in English.

Step 1
Handle the basic case of 0 through 99.
If the input to the program is 22, then the output should be 'twenty-two'.
Your program should complain loudly if given a number outside the blessed range.
Some good test cases for this program are:
0
14
50
98
-1
100

Step 2
Implement breaking a number up into chunks of thousands.
So 1234567890 should yield a list like 1, 234, 567, and 890, while the far simpler 1000 should yield just 1 and 0.
The program must also report any values that are out of range.

Step 3
Now handle inserting the appropriate scale word between those chunks.
So 1234567890 should yield '1 billion 234 million 567 thousand 890'
The program must also report any values that are out of range. It's fine to stop at "trillion".

Step 4
Put it all together to get nothing but plain English.
12345 should give twelve thousand three hundred forty-five.
The program must also report any values that are out of range."""

one_to_19 = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
             14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
tens_to_99 = {20: "twenty", 30: "thirty", 40: "fourty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
hundreds_number = [100, 200, 300, 400, 500, 600, 700, 800, 900]

def into_groups(number):
    num_str = str(number)
    group = [int(num_str[::-1][i:i+3][::-1]) for i in range(0, len(num_str), 3)][::-1]
    return group
    
def zero_to_99(number):
        number_str = str(number)
        number_say = ""
        if 0 <= number < 20:
            return one_to_19[number]
        if 20 <= number < 100:
            new_int = int(number_str[0] + "0") 
            number_say += tens_to_99[new_int]
            if 0 < int(number_str[-1]) <= 9:
                number_say = number_say + "-" + one_to_19[int(number_str[-1])] 
        return number_say
    
def hundreds(number):
    number_str = str(number)
    hundreds_say = ""
    if 0 < number < 100 or number in hundreds_number:
        return zero_to_99(int(number_str[0])) + " " + "hundred"
    if 100 < number < 1000:
        hundreds_say = hundreds_say + zero_to_99(int(number_str[0])) + " " + "hundred"
        hundreds_say = hundreds_say + " " + zero_to_99(int(number_str[1:3]))
    return hundreds_say
    
def say(number):
    grouped = into_groups(number)
    if 0 > number or number >= 999999999999:
        raise ValueError("input out of range")
    if 0 <= number < 100:
        return zero_to_99(number)
    if 100 <= number < 1000:
        return hundreds(number)
    if len(grouped) == 2:
        if "000" in str(number):
            return zero_to_99(int((str(number))[0])) + " thousand"
        if 0 < len(str(grouped[0])) <=2 :
            return zero_to_99(int(grouped[0])) + " thousand " + hundreds(int(grouped[1]))
        return hundreds(int(grouped[0])) + " thousand " + hundreds(int(grouped[1]))
    if len(grouped) == 3:
        if "000000" in str(number):
            return zero_to_99(int((str(number))[0])) + " million"
        if 0 < len(str(grouped[0])) <= 2:
            return zero_to_99(int(grouped[0])) + " million " + hundreds(int(grouped[1])) + " thousand " + hundreds(int(grouped[2]))
        return hundreds(int(grouped[0])) + " million " + hundreds(int(grouped[1])) + " thousand " + hundreds(int(grouped[1]))
    if len(grouped) == 4:
        if len(str(grouped[0])) <= 2:
            return zero_to_99(int(grouped[0])) + " billion " + hundreds(int(grouped[1])) + " million " + hundreds(int(grouped[2])) + " thousand " + hundreds(int(grouped[2]))
        return hundreds(int(grouped[0])) + " billion " + hundreds(int(grouped[1])) + " million " + hundreds(int(grouped[2])) + " thousand " + hundreds(int(grouped[2]))
    
answer = say(1000000)
print(answer)