"""
written by: Adrian Scholand 2022-12-22
"""

######################################## Packages importieren ########################################
import os
import numpy as np #wichtig um Daten einzulesen , np.array(), man kann mit arrays rechnen. Mit Listen gibt es häufig Probleme
import matplotlib.pyplot as plt
from kafe2 import XYContainer, Fit, Plot, ContoursProfiler
import math
from math import log10 , floor # damit man nicht math.log10 oder math.floor schreiben muss
import tabulate as tabulate
import latex_table as tab #benötigt die Python-Datai zum Latex-Tabellen erstellen von Oliver Cordes
import pandas as pd #nützlich um Tabellen im Notebook auszugeben


######################################## Funktionen definieren ########################################

#################### Werte Drucken ####################
#Drucken_Wert = True
def printwert(Variable, Einheit, Wert, Drucken_Wert): #Variable und Einheit sind Strings; Wert ist z.B. ein float
    if Drucken_Wert == True:
        print(Variable,"in",Einheit+":", Wert)
#a = 1.234
#printwert("a", "meter", a)

#################### Fehler Drucken ####################
#Drucken_Fehler = True
def printfehler(Variable, Einheit, Fehlerwert, Drucken_Fehler):
    if Drucken_Fehler == True:
        print("Fehler auf",Variable,"in",Einheit+":", Fehlerwert)
#a_err = 0.5678
#printfehler("Strecke a", "meter", a_err)

#################### item zwischen Elemente in Liste einfügen ####################
def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

#################### Werte auf 3 signifikante Stellen runden ####################
def round_it(x, sig):
    if x == 0: # da die Runden-Funktion nicht bei 0 Funktioniert
        return 0
    elif x > 0:
        return round(x, sig-int(floor(log10(abs(x))))-1)
    elif x < 0:
        return round(x, sig-int(floor(log10(abs(x))))-1)
    elif math.isnan(x):
        return x
    else:
        return "error"

########## Beispiele ##########
#a = 1.234                    #
#print(round_it(a), 3))       #
# >> 1.23                     #
#a2 = -1.234                  #
#print(round_it(a2, 3))       #
# >> -1.23                    #
#a3 = 0.0000                  #
#print(round_it(a3, 3))       #
# >> 0                        #
###############################

#################### Elemente in Liste auf 3 signifikante Stellen runden ####################
def round_list(list,k):
    list_rounded = []
    for element in list:
        if type(element) == float or np.float64:
            a = round_it(element,k)
            list_rounded.append(a)
        else:
            #print("Error in round_list: element is", type(element))
            list_rounded.append(element)
    return list_rounded

########## Beispiele ##########
#a1 = [1.234, 5.678]          #
#print(round_list(a1, 3))     #
# >> [1.23, 5.68]             #
###############################

#################### .0 von Float abschneiden ####################
def cutpointzero(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num
    
#################### .0 von Float abschneiden in einer Liste ####################
def cutpointzerolist(list):
    list_cutted = []
    for num in list:
        a = cutpointzero(num)
        list_cutted.append(a)
    return list_cutted