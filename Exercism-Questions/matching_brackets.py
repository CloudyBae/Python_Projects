"""Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, verify that any and all pairs are matched and nested correctly. 
The string may also contain other characters, which for the purposes of this exercise should be ignored."""

def is_paired(input_string):
    brackets = {
        "{": "}",
        "[": "]",
        "(": ")"
    }
    stack = []
    
    for i in input_string:
        if i in brackets.keys():
            stack.append(i)
            
        elif i in brackets.values():
            if not stack or brackets[stack.pop()] != i:
                return False
    
    return len(stack) == 0