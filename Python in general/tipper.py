# Creator: Ivan Sharma.
# Date: 15th December 2019.
# Desc: Calculate tips for restaraunt bill.


bill = input('Enter bill amount:')
bill = float(bill)
tips15 = 15/100*bill 
print('15% tip =',tips15)
tips20 = 20/100*bill
print('20% tip =',tips20)
pay15 = bill+tips15
print('Total amount paid with 15% tip =',pay15)
pay20 = bill+tips20
print('Total amount paid with 20% tip =',pay20)





