# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:57:51 2020

@author: CXZ
"""

from factory import Factory
from sql import Query
import logging

def main():
    try:
        query = Query("Customers")
        query.add_condition(Factory("Company name", "equals", "abc", "None"))
        query.add_condition(Factory("Contact title", "not equals", "love", "and"))
        query.add_condition(Factory("Phone", "contains", "6", "or"))
        query.to_sql()
    except Exception as e:
        logging("输入有误")

if __name__ == '__main__':
    main()
    
        