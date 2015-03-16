'''
Created on Feb 13, 2015
Takes dates in the format month/day/year and changes
them to ISO format year-month-day
@author: John Deyrup
'''

import csv
 
def read_csv(csv_name):
    '''
    Opens a csv file and stores it contents
    in a list
    '''
    in_list = []
    with open(csv_name, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
        for row in csvreader:
            in_list.append(row)
    return in_list
             
def write_csv(csv_name, table):
    '''
    Writes a table to csv file
    '''
    with open(csv_name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ',', lineterminator='\n')
        csvwriter.writerows(table)
 
def convert_num(a_num):
    '''
    Converts numbers less than 10
    into strings of the format 0X
    '''
    if(int(a_num) < 10):
        str_int = "0" + a_num
        return str_int
    else:
        return a_num
     
def split_dates(lst):
    '''
    Splits dates in the format month/day/year and changes 
    the date in ISO format year-month-date
    '''
    output_list = []
    for row in lst:
        row_list = []
        for date in row:
            if "/" in date:
                split_date = date.split("/")
                row_list.append(split_date[2]+"-"+convert_num(split_date[0])+"-"+convert_num(split_date[1])) 
            else:
                row_list.append(date)
        output_list.append(row_list)
    return output_list

def change_months_to_numbers(table):
    months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06",
              "Jul":"07","Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
    output_list = []
    for row in table:
        row_list = []
        for date in row:
            for key in months:
                if key in date:
                    split_date = (date.split("-"))
                    if len(split_date) == 3:
                        row_list.append("20"+split_date[2]+"-"+months[key]+"-"+convert_num(split_date[0]))
                    elif len(split_date) == 2:
                        row_list.append("20"+split_date[1]+"-"+months[key])
                    break
            else:
                row_list.append(date)
        output_list.append(row_list)
    return output_list

#Rename combinedlist.csv to your csv file name path  
mylist = read_csv('CombinedList.csv')
fix_months = change_months_to_numbers(mylist)
write_csv('converted_date.csv', split_dates(fix_months))
