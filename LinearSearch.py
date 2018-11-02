#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 15:39:43 2018

@author: soton
"""

data = [5,10,100,124,90,120,2,4,65,222,123]

def linearSearch(searchData,searchItem):
    
    count = 0;
    for item in searchData:
        if item == searchItem:
            print("Item Found")
            break;
        else:
            count = count + 1
    if count == len(searchData):
        print("Item Not Found")
            

def main():
    linearSearch(data,95)

if __name__== "__main__":
    main()