#!/usr/bin/env python3
#
# Import sys
import sys

Base_num = 3500
Input_money = sys.argv[1]

# catch ValueError
# catch ParameterError

try:
    if len(sys.argv[1:]) == 1:
        input_money = int(Input_money)
    else:
        print("Parameter Error")
        sys.exit(1)
except ValueError:
    print("ValueError:{}".format(Input_money))
else:
    tax_total = (input_money - Base_num)
    if tax_total < 0:
        amount_tax = (tax_total * 0) - 0 
    elif tax_total <= 1500:
        amount_tax = (tax_total * 0.03) - 0
    elif 1500 < tax_total <= 4500:
        amount_tax = (tax_total * 0.10) - 105
    elif 4500 < tax_total <= 9000:
        amount_tax = (tax_total * 0.20) - 555
    elif 9000 < tax_total <= 35000:
        amount_tax = (tax_total * 0.25) - 1005
    elif 35000 < tax_total <= 55000:
        amount_tax = (tax_total * 0.30) - 2755
    elif 55000 < tax_total <= 80000:
        amount_tax = (tax_total * 0.35) - 5505
    elif tax_total > 80000:
        amount_tax = (tax_total * 0.45) - 13505
    print("{:.2f}".format(amount_tax))
      

