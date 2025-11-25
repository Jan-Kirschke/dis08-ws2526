# Data Cleaning

> [!NOTE]
> In the following, you will parse information from text-based files with the command line, Unix tools, and Python. Please note that even though the files are provided as structured CSV files you are not supposed to simply read out the columns, but you should use regular expressions instead.

## Parsing contact information from the command line

In this directory, you will find a file called `csv/contacts.csv`. Use regular expressions to extract the following information from it.

Remember that you can use different tools like `grep`, `awk`, or `sed` to use regular expressions from the command line. Pipes might also be helpful. 

Document your commands and the corresponding outputs with verbatim formatting in a Markdown file called `parse_contacts.md`. Alternatively, you can write a bash script `parse_contacts.sh` with all commands.

1. Extract all email addresses from the text.
2. Extract all phone numbers from the text.
3. Extract all names that start with the letter ‘J’.
4. Extract all street names that contain the word 'St'.
5. Extract the last names of all people.
6. Extract all email domains (part after the @ sign).
7. Find all entries where the phone number ends with ‘7’.
8. Extract all instances of first names that end with the letter 'e'.

## Parsing product orders with Python

In this directory, you will find another file called `csv/orders.csv`. The following code snippet reads the file and parses all numbers with a regular expression. 

```python 
import re 


def main():
    
    # Read the CSV file with the product orders
    with open('./csv/orders.csv') as f_in:
        text = f_in.read()

    # Define the regular expression to extract all order numbers
    regex = r'\d+'

    # Match the regex with the text
    orders = re.findall(regex, text)

    # Print the results
    print(orders)
    

if __name__ == '__main__':
    main()
```

Please extend and reuse the code snippet such that the following details can be extracted from the CSV file. 

1.	Extract all order numbers from the text. 
2.	Extract all product codes.
3.	Extract all prices.
4.	Extract all order dates.
5.	Find all orders for products priced over $500. (You are allowed to use Python to filter the list.)
6.	Change the date format to DD/MM/YYYY. (Note the re.sub() method)
7.	Find all orders with the highest number of ordered items.
8.	Find the cheapest order(s). (You may want to use Python's min() method.)

Provide your answers in a Jupyter notebook called `parse.ipynb`.

> [!IMPORTANT]
> - Commit ither a Markdown file `parse_contacts.md` or a bash script `parse_contacts.sh` that contains the regex expressions and commands to parse the contacts from `csv/contacts.csv`. 
> - Commit an executable Jupyter notebook `parse.ipynb` that gives answers to the questions about the ordered products.