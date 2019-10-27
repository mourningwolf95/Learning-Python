# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 22:29:27 2019

@author: mourn
"""
with open("TestSave.txt", "r") as file:
    Save = file.readlines()

Name = Save.pop()
Char = Save.pop(0)
print(Name)