import re

list = ["1", "2", "3", "4", "5", "6", "7", "8", "8",  "9", "10"]

def remove_duplicates(list):
    for i in range(len(list)):
        for n in range(len(list)):
            if list[i] == list[n]:
                list.remove(list[i])

def find_max_min(list):
    return max(list), min(list)

#############################################################################################

transactions = [
    {'type': 'purchase', 'amount': 100, 'date': '2018-04-02'},
    {'type': 'sale', 'amount': 30.5, 'date': '2018-04-02'},
]

transaction_type = transactions[0]['type']
transaction_amount = transactions[0]['amount']
transaction_date = transactions[0]['date']

def list_of(my_key):
    amount_values = [transaction['amount'] for transaction in transactions]
    print(list_of('amount'))

def find_all(my_key, my_value):
    return [transaction for transaction in transactions if transaction[my_key] == my_value]
my_transactions = find_all('date', '2018-04-02')
print(my_transactions)
print(len(my_transactions))

def is_valid_date_format(date_string):
    date = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    result = date.match(date_string)
    return result != None