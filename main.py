import sys
import datetime
from functions import *

def main():
    dir = os.path.abspath('.')
    filename = 'expenses.csv'
    file_path = os.path.join(dir, filename)

    if (os.path.exists(file_path) == False): 
        with open(file_path, encoding='utf-8', mode='w') as f:
            f.write('#,name,amount,date\n')

    args = sys.argv

    if len(args) == 2:
        match args[1]:
            case '--list':
                list_expenses(file_path)
                return
            case '--total':
                print(get_total(file_path))
                return

    if (len(args) == 3):
        if args[1] == '--delete':
            delete_record(file_path, args[2])
            return
        
        date = datetime.datetime.now()
        date = str(date).split(" ")[0]

        new_record = {
            "number": len(get_expenses(file_path)),
            "name": args[1],
            "amount": args[2],
            "date": date
        }

        add_record(file_path, new_record)

main()

