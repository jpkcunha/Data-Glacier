# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 19:43:50 2022

@author: JOAO
"""

import pickle
import os
path = "C:/Users/JOAO/Documents/Data Glacier/DataGlacier/Week0/Serialization/"
os.chdir(path)


class Employee:
    
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal    
        self.eaddr = eaddr
        
    def display(self):
        print('Number: {}\nName: {}\nSalary: {:.2f}\nAddress: {}'
              .format(self.eno, self.ename, self.esal, self.eaddr))

emp = Employee(101, 'John', 4500, 'NYC')

with open('emp.pkl', 'wb') as f:
    pickle.dump(emp, f)
    print('Serialization done')
    
    
#%% Deserialization

with open('emp.pkl', 'rb') as f:
	obj = pickle.load(f)
	obj.display()