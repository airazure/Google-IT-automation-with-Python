#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
        with open(csv_file_location) as file_contents:
                csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
                employees_dict = csv.DictReader(file_contents, dialect = 'empDialect')
                employee_list = [data for data in employees_dict]
                return employee_list

employee_list = read_employees('/home/student-04-5323d6632c62/data/employees.csv')
print(employee_list)






#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
        with open(csv_file_location) as file_contents:
                csv.register_dialect('empDialect', skipinitialspace=True, str$
                employees_dict = csv.DictReader(file_contents, dialect = 'emp$
                employee_list = [data for data in employees_dict]
                return employee_list

employee_list = read_employees('/home/student-04-5323d6632c62/data/employees.$
print(employee_list)

def process_data(employee_list):
        department_list = [employee_data['Department'] for employee_data in e$
        #return department_list
        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(depa$
        return department_data

d_count = process_data(employee_list)
print(d_count)