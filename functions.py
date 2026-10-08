import os
import csv

def get_expenses(path):
    if os.path.exists(path):
        with open(path, mode='r') as f:
            lines = f.readlines()
            return lines
    else:
        print('incorrect filepath')

def list_expenses(path):
    expenses = get_expenses(path)
    for e in expenses:
        print(e)

def add_record(path, record):
    if os.path.exists(path):
        with open(path, mode='a') as f:
            f.write(f"{record["number"]},{record["name"]},{record["amount"]},{record["date"]}\n")
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


def delete_record(path, record_number):
    with open(path, newline='') as f:
        new_records = []
        reader = csv.reader(f)
        next(reader, None) # This skips the header
        for number, name, amount, date in reader:
            if number != record_number:
                new_records.append({
                    "number": None,
                    "name": name,
                    "amount": amount,
                    "date": date
                })

        for i in range(0, len(new_records)):
            new_records[i]["number"] = i + 1

        with open(path, mode='w') as f:
            f.write('number,name,amount,date\n')
    
        for r in new_records:
            add_record(path, r)