from tabulate import tabulate
from typing import List
def printOut(rows):
    if not rows:
        print("No data to display")
        return
    
    # The first row contains the column headers
    headers = rows[0]
    data = rows[1:]
    
    # Print the table
    print(tabulate(data, headers=headers, tablefmt="pretty"))
def can_be_int(v) : 
    try : 
         v = int(v)
         return True
    except : 
         return False
def Conditional(row: List[str], columns: List[str], argument: List[str]):
    if argument == [] : 
        return True
    # Ensure all elements in row are strings and properly quoted
    row = [f"'{item}'" if not item.isdigit() else item for item in row]
    
    code = f"""
{",".join(columns)} = {",".join(row)}
c = {" ".join(argument)}
"""    
    exec_env = {}
    exec(code, {}, exec_env)
    
    return exec_env["c"]


def cleanInput(fieldArray) :
        field = []
        for r in fieldArray : 
            if "," in r : 
                field.extend([e.strip() for e in r.split(",")])
                continue
            field.append(r.strip())
        field = list(filter(lambda x : x!='', field))
        return field
    