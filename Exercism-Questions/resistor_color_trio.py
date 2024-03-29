"""In resistor-color duo you decoded the first two colors. For instance: orange-orange got the main value 33. 
The third color stands for how many zeros need to be added to the main value. The main value plus the zeros gives us a value in ohms. 
For the exercise it doesn't matter what ohms really are. For example:

orange-orange-black would be 33 and no zeros, which becomes 33 ohms.
orange-orange-red would be 33 and 2 zeros, which becomes 3300 ohms.
orange-orange-orange would be 33 and 3 zeros, which becomes 33000 ohms.
(If Math is your thing, you may want to think of the zeros as exponents of 10. If Math is not your thing, go with the zeros. 
It really is the same thing, just in plain English instead of Math lingo.)

This exercise is about translating the colors into a label:
"... ohms"

So an input of "orange", "orange", "black" should return:
-"33 ohms"

When we get to larger resistors, a metric prefix is used to indicate a larger magnitude of ohms, such as "kiloohms". 
That is similar to saying "2 kilometers" instead of "2000 meters", or "2 kilograms" for "2000 grams".

For example, an input of "orange", "orange", "orange" should return:
-"33 kiloohms" """

dict = {"black":0, "brown":1, "red":2, "orange":3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}

def label(colors):
    one = str(dict[colors[0]])
    two = str(dict[colors[1]])
    value = one + two
    for i in range(dict[colors[2]]):
        value += "0"
    new_value = int(value)

    if new_value < 1000:
        return f"{new_value} ohms"
    if 1000 <= new_value < 1000000:
        result = int(value.replace("0", "", 3))
        return f"{result} kiloohms"
    if 1000000 <= new_value < 1000000000:
        result = int(value.replace("0", "", 6))
        return f"{result} megaohms"
    if 1000000000 <= new_value < 1000000000000:
        result = int(value.replace("0", "", 9))
        return f"{result} gigaohms"
    