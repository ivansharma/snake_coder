# Creator: Ivan Sharma.
# Date: 16th December 2019.
# Desc: Calculate weekly payments.


Weekly_rent = input('How much is your weekly rent? ')
Weekly_rent = float(Weekly_rent)
Bus_fare = input('How much is your weekly bus fare? ')
Bus_fare = float(Bus_fare)
Grocery_costs = input('How much did you pay for groceries last week? ')
Grocery_costs = float(Grocery_costs)
Total_payment = Weekly_rent+Bus_fare+Grocery_costs
Total_payment = round(Total_payment,2)
print(Total_payment)
