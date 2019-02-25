#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 12:19:17 2018

@author: soton
[['Jerry Seinfeld', '(212) 344-3784'], ['Cosmo Kramer', '(212) 559-8185']]
"""

import os
import csv

phoneList = [] 
phone_header = [ 'Name', 'Phone Number']
index = -100
name_pos = 0
phone_pos = 1

#%%
def main_loop():
   load_phone_list()
   while 1:
       choice = db_showMenu()
       if choice == None:
            continue
       elif choice == "s":
           db_show()
       elif choice == "n":
           db_new()
       elif choice == "d":
          which = input("Which item do you want to delete? ")
          print("which is ", which)
          db_delete(which)
       elif choice == "e":
           db_edit()
       elif choice == "r":
           reorder_phones()
       elif choice == "q":
           print("quitting...")
           break;
       else:
           print("Invalid Choice")
           
   save_phone_list()

"""
"""
#%%

def db_showMenu():
    print("Choose one of the following options?")
    print("   s) Show")
    print("   n) New")
    print("   d) Delete")
    print("   e) Edit")
    print("   q) Quit")
    print("   r) Reorder")
    
    choice = input("Choice: ")    
    if choice.lower() in ['n','d', 's','e', 'q','r']:
        return choice.lower()
    else:
        print(choice +"?" + " That is an invalid option!!!")
        return None
"""
"""
#%%
def save_phone_list():
    f = open("myphones.csv", 'w', newline='')
    for item in phoneList:
        csv.writer(f).writerow(item)
    f.close()
"""
"""
#%%
    
def load_phone_list():
    if os.access("myphones.csv",os.F_OK):
        f = open("myphones.csv")
        for row in csv.reader(f):
            phoneList.append(row)
        f.close()
"""
"""
#%%

def show_phone(phone, index):
    outputstr = "{0:>3}  {1:<20}  {2:>16}"
    print(outputstr.format(index, phone[name_pos], phone[phone_pos]))

"""
"""
#%%

def db_show():
    show_phone(phone_header, "")
    _index = 0
    for phone in phoneList:
        show_phone(phone,str(_index+1))
        _index = _index + 1
"""
"""
#%%

def db_new():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    tempPhoneList = [name,phone]
    phoneList.append(tempPhoneList)
    print("New")
"""
"""
#%%

def proper_menu_choice(which):
    if not which.isdigit():
        print ("'" + which + "' needs to be the number of a phone!")
        return False
    which = int(which)
    if which < 1 or which > len(phoneList):
        print ("'" + str(which) + "' needs to be the number of a phone!")
        return False
    return True
    
"""
"""

def db_delete(which):
    deleteIndexStr = input("Enter Item Index you wish to delete: ")
    deletedIndex = int(deleteIndexStr)
    if (not proper_menu_choice(deletedIndex)):
        return
    del phoneList[which-1]
    print( "Deleted phone #", which)
"""
"""
#%%


def db_edit(which):
    phone = phoneList[which-1]
    print("Enter the data for a new phone. Press <enter> to leave unchanged.")
    
    print(phone[name_pos])
    newname = input("Enter phone name to change or press return: ")
    if newname == "":
        newname = phone[name_pos]
        
    print(phone[phone_pos])    
    newphone_num = input("Enter new phone number to change or press return: ")
    if newphone_num == "":
        newphone_num = phone[phone_pos]
            
    phone = [newname, newphone_num]
    phoneList[which-1] = phone
    
"""
"""
#%%
def reorder_phones():
    tempPhoneList = []
    for phone in phoneList:
        tempPhoneList.append(phone[0])
    tempPhoneList.sort(key = str.lower)

    listPhone = []
    for tempPhone in tempPhoneList:
        for phone in phoneList:
            if tempPhone == phone[0]:
                listPhone.append(phone)
    _index = 0
    for phone in listPhone:
        phoneList[_index] = phone
        _index = _index + 1
    print(phoneList)
   
"""
"""
#%%
#%%
# The following makes this program start running at main_loop() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()
#%%

    