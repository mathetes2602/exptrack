import os

def get_expenses(path):
    if os.path.exists(path):
        with open(path, mode='r') as f:
            lines = f.read()
            return lines
    else:
        print('incorrect filepath')

def list_expenses(path):
    expenses = get_expenses(path)
    print(expenses)

def add_record(path, record):
    if os.path.exists(path):
        with open(path, mode='a') as f:
            f.write(f"{record["name"]},{record["amount"]},{record["date"]}\n")
    else:
        print('incorrect filepath')

def get_total(path):
    if os.path.exists(path):
        with open(path, mode='r')as f:
            total = 0 
            lines = f.readlines()
            for line in lines[1:]:
                cells = line.split(',')
                total += int(cells[1])
            return total


