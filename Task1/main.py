import csv
from statistics import mean

def read_data(file_path, is_skip_header=True):
    data = []
    
    # Read the CSV file
    try:   
        with open(file_path, mode ='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            # Skip the header column
            if is_skip_header:
                next(reader)
            
            # Get age of each person
            for line in reader:
                _, age = line
                data.append(age)
                
    except OSError:
        print("Cannot open file: {}".format(file_path))
        
    return data

def cal_avg_age(file_path):
    data = read_data(file_path)
    if not data:
        return 0
    
    # Convert age from string to int    
    ages = []
    for age in data:
        if age is not None:
            try:
                ages.append(int(age))
            except ValueError:
                continue
    if not ages:
        return 0
    
    return mean(ages)

if __name__ == "__main__":
    avg_age = cal_avg_age('data.csv')
    print(avg_age)