import sys
import datetime
from functions import *


dir = os.path.abspath('.')
filename = 'expenses.csv'
file_path = os.path.join(dir, filename)

if (os.path.exists(file_path) == False): 
    with open(file_path, encoding='utf-8', mode='w') as f:
        f.write('name,amount,date\n')

args = sys.argv

if len(args) == 2:
    match args[1]:
        case '--list':
            list_expenses(file_path)
        case '--total':
            print(get_total(file_path))

if (len(args) == 3):
    date = datetime.datetime.now()
    date = str(date).split(" ")[0]

    new_record = {
        "name": args[1],
        "amount": args[2],
        "date": date
    }

    add_record(file_path, new_record)

