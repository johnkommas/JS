# Εισοδος
# Επεξεργασία
# Έξοδος


sales_price = abs(float(input('Sales Price:')))
discount = abs(int(input('Discount: ')))

discount_value = sales_price * (discount / 100)
final_sales_price = sales_price - discount_value

print(f"""
Sales Price:\t\t : {sales_price} EUR
Discount:\t : {discount} %
Discount Value: \t : {discount_value} EUR
Final Sales Price: \t : {final_sales_price} EUR
""")
