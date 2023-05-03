"""Your task is to implement a binary search algorithm.

A binary search algorithm finds an item in a list by repeatedly splitting it in half, only keeping the half which contains the item we're looking for. 
It allows us to quickly narrow down the possible locations of our item until we find it, or until we've eliminated all possible locations.

The algorithm looks like this:

Find the middle element of a sorted list and compare it with the item we're looking for.
If the middle element is our item, then we're done!
If the middle element is greater than our item, we can eliminate that element and all the elements after it.
If the middle element is less than our item, we can eliminate that element and all the elements before it.
If every element of the list has been eliminated then the item is not in the list.
Otherwise, repeat the process on the part of the list that has not been eliminated."""

def find(search_list, value):
    sorted_list = sorted(search_list)    
    
    if value not in search_list:
        raise ValueError("value not in array")

    while len(sorted_list) >= 1:
        middle = len(sorted_list)//2
        if (len(sorted_list) == 1) and (value == sorted_list[0]):
            return search_list.index(value)
        
        elif sorted_list[middle] == value:
            return search_list.index(value)
          
        elif sorted_list[middle] > value:
            sorted_list = sorted_list[:middle]
        
        elif sorted_list[middle] < value:
            sorted_list = sorted_list[middle+1:]  
