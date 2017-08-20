#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print enron_data[enron_data.keys()[0]].keys()
s = 0
e = 0
for k,v in enron_data.items():
    if(v['salary'] != 'NaN'):
        s += 1
    if(v['email_address'] != 'NaN'):
        e += 1
        
print 'Emails: ', e, 'Salary: ', s

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['total_payments']   
for k,v in enron_data.items(): 
   if 'FASTOW' in k:
       print v['total_payments']
for k,v in enron_data.items(): 
   if 'LAY' in k:
       print v['total_payments']
       
print enron_data['FASTOW ANDREW']['total_payments']
print enron_data['LAY KENNETH']['total_payments']
count = 0
for i in enron_data:
    if (enron_data[i]['poi'] == 1):
        count+=1
        
print count
results = []
with open('../final_project/poi_names.txt') as inputfile:
    for line in inputfile:
        count+=1
print count


payments_zero = len(dict((key,val) for key,val in enron_data.items() if val['total_payments'] == 'NaN'))
percentage = (float) (payments_zero) / len(enron_data) * 100
print percentage




