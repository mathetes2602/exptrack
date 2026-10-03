from functions import *

dir = os.path.abspath('.')
filename = 'expenses.csv'
file_path = os.path.join(dir, filename)

new_record = {
    "name": "new expense",
    "amount": 1234,
    "date": "03/10/26",
}
add_record(file_path, new_record)
list_expenses(file_path)



