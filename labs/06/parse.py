import pandas as pd
import re

"""
1.	Extract all order numbers from the text. 
2.	Extract all product codes.
3.	Extract all prices.
4.	Extract all order dates.
5.	Find all orders for products priced over $500. (You are allowed to use Python to filter the list.)
6.	Change the date format to DD/MM/YYYY. (Note the re.sub() method)
7.	Find all orders with the highest number of ordered items.
8.	Find the cheapest order(s). (You may want to use Python's min() method.)
"""

def main(regex, title):
    sep = "_"*80 + "\n"
    
    with open('labs/06/csv/orders.csv') as f_in:
        text = f_in.read()
    print(text)
    results = re.findall(regex, text)
    print(title,"\n",results,"\n",sep)

    

if __name__ == '__main__':
    #main(r"\d+", "\n1. Extract all order numbers from the text.")
    #main(r"[a-zA-Z0-9]{12}", "2. Extract all product codes.")
    #main(r"\$\d+.\d+", "3. Extract all prices.")
    #main(r"\d+/\d+/\d+", "4. Extract all order dates.")
    #main(r"\$[56789]\d+.\d+", "5. Find all orders for products priced over $500.")
    for datum in main(r"\d+/\d+/\d+", "6. Change the date format to DD/MM/YYYY."):
        print(re.sub(datum, )))
