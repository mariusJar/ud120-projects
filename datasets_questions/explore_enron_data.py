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
# import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print("People in data set:", len(enron_data))
print("Features in people data set:", len(enron_data.itervalues().next()))

poiCount = 0
salaryCount = 0
emailCount = 0
noTotalPaymentCount = 0
poisWithNoTotalPaymnetCount = 0
for key, value in enron_data.iteritems():
    if value["total_payments"] == "NaN":
        noTotalPaymentCount = noTotalPaymentCount + 1
    
    # if not math.isnan(value["salary"]):
    if value["salary"] != "NaN":
        salaryCount = salaryCount + 1

    if value["email_address"] != "NaN":
        emailCount = emailCount + 1
    
    if value["poi"] == 1:
         poiCount = poiCount + 1
         if value["total_payments"] == "NaN":
             poisWithNoTotalPaymnetCount = poisWithNoTotalPaymnetCount + 1
        #  print("Name of poi:", key)
         
print("Number of pois:", poiCount)
print("Count of known salaries:", salaryCount)
print("Count of known emails:", emailCount)
print("No total payments found count:", noTotalPaymentCount)
print("No payment percentage:", noTotalPaymentCount * 100 / len(enron_data))
print("POIs with no total payments found count:", poisWithNoTotalPaymnetCount)
print("POIs with no payment percentage:", poisWithNoTotalPaymnetCount * 100 / poiCount)
# print("James Prentice:", enron_data["PRENTICE JAMES"])
# print("Wesley Colwell:", enron_data["COLWELL WESLEY"])
# print("Kenneth Lay:", enron_data["LAY KENNETH L"])
# print("Jeffrey K Skilling:", enron_data["SKILLING JEFFREY K"])
# print("Andrew Fastow:", enron_data["FASTOW ANDREW S"])