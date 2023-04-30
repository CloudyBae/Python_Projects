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
    # lists are same length
    if list_one == list_two: 
        return EQUAL
    # list is superlist
    if len(list_one) > len(list_two):
        if sum(list_two) == 0:
            return SUPERLIST
            
        compare_list = list_one
        start = list_one.index(list_two[0])
        for i in range(len(list_two)):
            compare_list[start] = list_two[i]
            start += 1
            if compare_list == list_one:
                return SUPERLIST
            return UNEQUAL
    # list is sublist
    if len(list_one) < len(list_two):
        if sum(list_one) == 0:
            return SUBLIST
            
        compare_list = list_two
        start = list_two.index(list_one[0])
        for i in range(len(list_one)):
            compare_list[start] = list_one[i]
            start += 1
            if compare_list == list_two:
                return SUBLIST
            return UNEQUAL
    return UNEQUAL