# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:20:56 2024

@author: KOM
"""

# def Names():
names= open(r"C:/Users/KOM/Desktop/Opgaver/Names.txt")#definér sri hvor fil er gemt
names_data = names.read()
names_split=names_data.split("\n")  #split by line   
names_split.sort()

#Count letters in each name
counter = 0
#loop through names of each line
for name in names_split:
    # loop through each letter of each name
    for letters in name:
        # define the letters, both capital letters and lowercase letters
        if letters == 'J' or letters=='j':
            # 1 is added to a counter
            counter += 1
print(counter)