import sys
import datetime
from functions import *


dir = os.path.abspath('.')
filename = 'expenses.csv'
file_path = os.path.join(dir, filename)

args = sys.argv
if (len(args) == 2 and args[1] == "list"):
    list_expenses(file_path)
elif (len(args) == 3):
    date = datetime.datetime.now()
    date = str(date).split(" ")[0]

    new_record = {
        "name": args[1],
        "amount": args[2],
        "date": date
    }

    add_record(file_path, new_record)
else:
    print("wrong number of arguments")

