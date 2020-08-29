# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 22:46:51 2020

@author: CXZ
"""

class Factory:
    def __init__(self, attribute, relation, value, logic):
        self.attribute = attribute
        self.relation = relation  # == < > <= >= contains !=
        self.value = value
        self.logic = logic  # and/or
