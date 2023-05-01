"""Given any two lists A and B, determine if:
-List A is equal to list B; or
-List A contains list B (A is a superlist of B); or
-List A is contained by list B (A is a sublist of B); or
-None of the above is true, thus lists A and B are unequal
Specifically, list A is equal to list B if both lists have the same values in the same order. 
List A is a superlist of B if A contains a sub-sequence of values equal to B. 
List A is a sublist of B if B contains a sub-sequence of values equal to A."""

# Possible sublist categories.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"

def sublist(list_one, list_two):
    one = ','.join(map(str, list_one))
    two = ','.join(map(str, list_two))
    
    # lists are same length
    if list_one == list_two: 
        return EQUAL
    # list is superlist
    if len(list_one) > len(list_two):
        if one == "":
            return SUPERLIST
        if two in one:
            return SUPERLIST
        return UNEQUAL

    # list is sublist
    if len(list_one) < len(list_two):
        if two == "":
            return SUBLIST
        if one in two:
            return SUBLIST
        return UNEQUAL
    return UNEQUAL