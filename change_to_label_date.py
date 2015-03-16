'''
Created on Feb 20, 2015
Opens a csv, splits the dates, converts the month
to a roman numeral, and then puts the date back into
the format day.month.year
@author: John Deyrup
'''
import csv
def read_csv(csv_name):
    '''
    Opens a csv file and stores it contents
    in a list
    '''

    with open(csv_name, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        for row in csvreader:
            return row

def write_csv(csv_name, table):
    '''
    Writes a table to csv file
    Line terminator prevents their from
    being extra carriage returns (not sure what it does)
    '''
    with open(csv_name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ',', lineterminator='\n')
        csvwriter.writerow(table)

def convert_dates(table):
    '''
    Splits a date, then converts the month
    to a roman numeral. Then puts the date back together
    into the format day.month.year
    '''
    converted_table = []
    month_dic = {"01":"i", "02":"ii", "03":"iii", "04":"iv","05":"v","06":"vi","07":"vii",
                 "08":"viii","09":"ix","10":"x","11":"xi","12":"xii"}
    for elem in table:
        split_elem = elem.split("-")
        if len(split_elem) == 3:
            converted_table.append(str(int(split_elem[2]))+"."+month_dic[split_elem[1]]+"."+split_elem[0].strip())
        elif len(split_elem) == 2:
            converted_table.append(month_dic[split_elem[1]]+"."+split_elem[0].strip())
        else:
            print("unknown string length: " + elem)
    return converted_table
                
csv_table = read_csv('isodate.csv')
write_csv('change_date.csv',convert_dates(csv_table))
