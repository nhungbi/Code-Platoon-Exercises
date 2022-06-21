import os
import csv

##read info
def read_file(file_name):
    """
    Given a csv file name, return a list of dictionaries of all of thhe information.
    """
    list_info = [] #list of dictionary
    with open('data/'+file_name) as csv_file:
        reader = csv.DictReader(csv_file) #read row as dictionary, header denotes the key
        for row in reader: #row is a dict of with parameters to create Student
            list_info.append(row)

    return list_info
def pretty_info(list_dict):
    """
    Given a list of dictionary of information, return an english format of all of the information. 
    """
    pretty_string = ''
    for dict_ in list_dict:
        pretty_string +=  dict_['name'] + ' is a' +dict_[' age'] + ' years old' +  dict_[' breed'] + '.\n' 
    return pretty_string
user_question = input('What type of animal would you like information on? Enter in plural form. ')

try:
    data = read_file(user_question + '.csv')
    print(pretty_info(data))
except:
    print(f'Sorry, we don\'t have any {user_question} here.')