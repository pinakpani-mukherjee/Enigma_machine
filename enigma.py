#because i am bored in class, I am going to write the enigma machine coder in python
#lets see how it goes
#I will be makng the army model, with 3 roters
# I have to add plugboard settings and rotor settings
#let us first deal with the plug board, also known as the stecker board
#6 pairs were steckered each day, and the remining 14 were self steckered
#then we had the daily rotor use, ranging from 1~5
#then we had the ring settings
#then we had initial rotor positions


#let us now creat the steckerboard combinations
iterable_stecker = []
from itertools import combinations

comb = combinations("ABCDEFGHIJKLMNOPQRSTUVWXYZ",2)

for i in list(comb):
    iterable_stecker.append(i)
    
#creating my combination list
    
for i in range(25):
    globals()["list" + str(25-i)] = iterable_stecker[:(25-i)]
    iterable_stecker = iterable_stecker[(25-i):]
    
#creating my stecker collection

import random



#creating my stecker_book for a year
for i in range(365):
    random_selection = []

    while len(random_selection)!=6:
        r = random.randint(1,25)
        if r not in random_selection: random_selection.append(r)




plain_text = input("Please enter the text you want to be coded.")

