print("Welcome to the tip calculator!")
bill = float(input("What was the total of the bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_decimal = tip / 100
bill_tip = bill * tip_decimal
bill_total = bill + bill_tip
per_person = round(bill_total / people, 2)

print(f"Each person should pay: ${per_person}")