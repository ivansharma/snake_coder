# Creator: Ivan Sharma.
# Date: 21st December 2019.
# Desc: Calculate the GST(goods service tax).


base_price = input('Enter the base price of your goods/services: ')
base_price = float(base_price)
GST = (15/100) * base_price
print('Your GST is:',GST)
total_amount = base_price + GST
print('The total amount is:',total_amount)

