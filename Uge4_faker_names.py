# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:13:31 2024

@author: KOM
"""

from faker import Faker


fake=Faker(locale="da")

Names_list=[]
def Generate_names(Names):
    for i in range(1,Names):
   
        Names={}
        
        Names=fake.name()
        
        Names_list.append(Names)
        with open(r"C:/Users/KOM/Desktop/Opgaver\Names.txt", "w") as output: # definér hvilken sti den skal bruge
            for line in Names_list:
                output.write(str(line) + "\n")# gemmer i ny linje efter hver gennemgang
 
    
data = Generate_names(1000)