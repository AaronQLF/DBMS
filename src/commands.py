from StorageManager import StorageManager
from Utils import printOut,cleanInput,Conditional
class Commands : 
    def __init__(self) : 
        self.strg = StorageManager()
    
    def select(self,fieldarray ,table,condition = []) : 
        strg = self.strg
        res = strg.RetrieveTable(table.lower(),conditions= condition)

        if fieldarray == ["*"] : 
            return res
        else : 
            field= cleanInput(fieldarray)
            for i in field : 
                if i not in res[0] : 
                    raise Exception(f"Couldn't find the field {i} in table {table} ")
            return [[field]] + [[e[i]] for e in res[1:]] if len(field) == 1 else [field] + [[e[res[0].index(f)] for f in field] for e in res[1:]]
    def insert(self,values,table, formats) :
        strg = self.strg
        res = strg.RetrieveTable(table.lower())
        CleanedValues = (self.cleanInput(values))
        if len(res[0]) != len(CleanedValues) : 
            raise Exception(f"Expected {len(res[0])} rows, found {len(CleanedValues)} rows")
        
        CleanedTemplate = self.cleanInput(formats)
        CleanedTemplate =[f.lower() for f in CleanedTemplate]
        temp = []
        print(CleanedTemplate,CleanedValues)
        if len(CleanedTemplate) != len(CleanedValues) : 
            raise Exception(f"Expected {len(CleanedTemplate)} rows for format, found {len(CleanedValues)} rows")
        for i in res[0] : 
            if i.lower() not in CleanedTemplate :
                raise Exception(f"Couldn't find {i} in given formats")
            else : 
                temp.append(CleanedValues[CleanedTemplate.index(i)])
        if len(temp) != len(res[0]) : 
            raise Exception(f"Expected {len(CleanedTemplate)} rows for format, found {len(CleanedValues)} rows")
        res.append(temp)
        printOut(res)
        strg.CreateTable(table,res[0],res[1:])
        return True

    def delete(self,table) :
        self.strg.DeleteTable(table)
        #delete table OR delete argument inside of the table
    def remove(self,table,conditions) : 
        self.strg.DeleteFromTable(table,conditions)
    def create(self,arguments) : 
        pass