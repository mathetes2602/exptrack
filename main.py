import os

dir = os.path.abspath('.')
filename = 'expenses.csv'
file_path = os.path.join(dir, filename)

if (os.path.exists(file_path) == False): 
    with open(file_path, encoding='utf-8', mode='w') as f:
        f.write('name,amount,date\n')

