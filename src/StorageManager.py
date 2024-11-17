import os
import csv
from Trie import *
from Utils import Conditional,printOut
class StorageManager : 

    def __init__(self) : 
        self.trie = Trie()
        if "dbms" not in os.listdir() : 
            os.mkdir("dbms")
        else : 
            #get all names
            for i in os.listdir("dbms") : 
                self.trie.insert(i.split(".")[0])
    def CreateTable(self, name,columns,values = []) -> bool : 
        try :
            if len(values[0]) != len(columns) and values != [] : 
                raise Exception("Rows and values length unmatched")
            if str(name + ".csv") in os.listdir("dbms"): 
                print("Table already Exists, Overwriting")
            with open(f"dbms/{name}.csv", mode ="w", newline='') as file : 
                writer = csv.writer(file)
                writer.writerow(columns)
                if values != [] :
                    writer.writerows(values)
            self.trie.insert(name)
            return True
        except Exception as e : 
            print(e)
            return False
    def DeleteTable(self,name) -> bool: 
        try : 
            if str(name + ".csv") not in os.listdir("dbms"): 
                raise Exception(f"Table doesn't exist, the closest matches are {c}" if (c:=self.trie.closest(name)) != [] else "Table doesn't exist")
            os.remove(f"dbms/{name}.csv")
            self.trie.delete(name)
            return True
        except Exception as e : 
            print(e)
            return False
    def DeleteFromTable(self,name,conditions = []) : 
        tbl= self.RetrieveTable(name,conditions,False)
        printOut(tbl)
        self.CreateTable(name,tbl[0],tbl[1:])

    def RetrieveTable(self,name,conditions= [], include = True) -> list[list[str]] : 
        if not self.trie.contains(name) : 
            raise Exception(f"Table doesn't exist, the closest matches are {c}" if (c:=self.trie.closest(name)) != [] else "Table doesn't exist")
        try : 
            res =[]
            with open(f"dbms/{name}.csv", mode= "r", newline='') as file :
                spamreader = csv.reader(file,delimiter=",")
                for i,row in enumerate(spamreader) : 
                    if i == 0 : 
                        field = row
                        res.append(row)
                        continue
                    if (not include and not Conditional(row,field,conditions)) or (include and Conditional(row,field,conditions)):
                        res.append(row)
            return res
        except Exception as e : 
            print(e)
            
    


