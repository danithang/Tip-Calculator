#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Write your code below this line 
print("Welcome to the Tip Calculator")
#float is used because the total bill will have decimal
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 15, 20? "))
split_bill = int(input("How many people to split the bill? "))
a = total_bill * percentage_tip / 100

b = (total_bill + a) / split_bill
#rounding the answer in 2 decimals places
#another way to round is: final_bill = round(b,2)
final_bill = "{:.2f}".format(b)               
print(f"Each person should pay: ${final_bill}")