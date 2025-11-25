from traceback import print_tb
import pandas as pd

contacts = pd.read_csv("labs/06/csv/contacts.csv")
orders = pd.read_csv("labs/06/csv/orders.csv")

print(orders.head(4))
