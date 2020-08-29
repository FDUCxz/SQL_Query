# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:49:51 2020

@author: CXZ
"""

from factory import Factory
from sql import Query

if __name__ == "__main__":
    company_name = ["aaa", "bbb", "ccc"]
    contact_title = ["x" , "y" , "z"]
    
    for i in range(3):
        query = Query("Customers")
        query.add_condition(Factory("Company name", "equals", company_name[i], "None"))
        query.add_condition(Factory("Contact title", "not equals", contact_title[i], "and"))
        query.add_condition(Factory("Phone", "contains", str(i), "or"))
        if query.to_sql() == "SELECT * FROM Customers WHERE Company name = " + company_name[i] +" and Contact title <> " + contact_title[i] + " or Phone like "+str(i):
            print("第{}次单元测试成功！".format(i+1))
        else:
            print("第{}次单元测试失败！".format(i+1))
        
