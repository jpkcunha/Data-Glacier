# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 19:50:11 2022

@author: JOAO
"""

import json
import os
path = "C:/Users/JOAO/Documents/Data Glacier/DataGlacier/Week0/Serialization/"
os.chdir(path)

employee = {'name': 'John', 'age': 55, 'salary': 4000.0, 'isMarried': True, 'isHavingCar': None}

json_string = json.dumps(employee, indent = 4)
print(json_string)

with open('emp.json', 'w') as f:
    json.dump(employee, f, indent = 4)
    
    
#%% Deserialization



with open('emp.json', 'r') as f:
    obj = json.load(f)
    print(type(obj))
    print(obj)