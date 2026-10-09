import os
import csv

def get_expenses(path):
    if os.path.exists(path):
        with open(path, mode='r') as f:
            lines = f.readlines()
            return lines
    else:
        print('incorrect filepath')

def get_max_padding(lines):
    max_padding = {
        "#": 0,
        "name": 0,
        "amount": 0,
    }
    for line in lines:
        line = line.strip()
        cells = line.split(',')
        if len(cells[0]) > max_padding["#"]:
            max_padding["#"] = len(cells[0])
        if len(cells[1]) > max_padding["name"]:
            max_padding["name"] = len(cells[1])
        if len(cells[2]) > max_padding["amount"]:
            max_padding["amount"] = len(cells[2])
    return max_padding

def get_padding(max_padding, cells):
    return {
        "#": max_padding["#"] - len(cells[0]),
        "name": max_padding["name"] - len(cells[1]),
        "amount": max_padding["amount"] - len(cells[2])
    }

def list_expenses(path):
    expenses = get_expenses(path)
    max_padding = get_max_padding(expenses)
    bottom_padding = max_padding["#"] + max_padding["name"] + max_padding["amount"] + 18 # date + spaces
    for e in expenses:
        e = e.strip()
        cells = e.split(',')
        pad = get_padding(max_padding, cells)
        print(f"{cells[0]}{pad["#"] * ' '}| {cells[1]}{pad["name"] * ' '}| {cells[2]}{pad["amount"] * ' '}| {cells[3]}")
        print(f"{bottom_padding * '-'}")

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
                total += int(cells[2])
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
            f.write('#,name,amount,date\n')
    
        for r in new_records:
            add_record(path, r)