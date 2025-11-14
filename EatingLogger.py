import datetime as datetime 
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
from dataclasses import dataclass
import json 

'''
The purpose of this program is to take the common foods I eat and create daily tallies of caloric intake and protein. 
It takes input from a basic GUI and converts that into JSON data that is then loaded for display, allowing me to export and import logs.
It must use GUI elements, who wants to use the command line for input? Tacky!



'''
@dataclass 
class food:
        name: str
        weight: int
        calories: int
        protein: float 

        def __str__(self):
                return self.name
class catalog: 
        
        def read_from_file(self, filename):
               self.food_list = []
               with open(filename) as f:
                    jsondata = json.load(f)

                    for dict in jsondata:
                        food_item = list(dict.values())
                        self.food_list.append(food(food_item[0], food_item[1], food_item[2], food_item[3]))

                    pass
               
        def __init__(self, filename):
                self.read_from_file(filename)

                

class datalog:
       
       def __init__(self, entrylist):
              self.entrylist = entrylist

       
       def newentry(self, entry):
              self.entrylist.append(entry)

@dataclass 
class entry:
       date: datetime 
       food: food 



              



x = catalog("catalog.json")
print(x.food_list)