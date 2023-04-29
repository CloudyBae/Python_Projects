"""use formula below to check if isbn is valid 
   (a * 10 + a * 9 + a * 8 + a * 7 + a * 6 + a * 5 + a * 4 + a * 3 + a * 2 + a * 1) mod 11 == 0"""

# make a list of the isbn numbers 
# if check character = X, the value is 10
# if there are other non X characters, invalid ISBN
def hyphen(isbn):
    no_dash = []
    for char in isbn:
        if char.isnumeric() == True: 
            no_dash.append(int(char))
        elif "X" in isbn[-1:]:  
            if char == "X":
                no_dash.append(10)
        else:
            if char.isalpha() == True:
                return False        
    return no_dash

# checks if the isbn is valid using the formula at the top
def is_valid(isbn):
    total = 0
    number = 10
    isbn_list = hyphen(isbn)
    if hyphen(isbn) == False:
        return False
    
    if len(isbn_list) != 10:
        return False
    
    for num in range(len(isbn_list)):
        total += (isbn_list[num] * number)
        number -= 1
    
    return total % 11 == 0