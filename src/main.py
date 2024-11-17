import sys
from commands import Commands
from Utils import printOut
args = [e.lower() for e in sys.argv[1:]]
#check the first one
Commands = Commands()

if args[0] not in ['select', 'insert', 'create', 'remove', 'delete']:
    raise Exception("Function Not recognized")
if args[0] == 'select':
    s=Commands.select(args[1:args.index("from")],args[args.index("from") +1], args[args.index("where")+1:] if "where" in args else [])
    #field, table
    printOut(s)
elif args[0] == 'insert':
    #insert, into
    print(args[1:args.index("into")], args[args.index("into")+1], args[args.index("format") +1:])
    Commands.insert(args[1:args.index("into")], args[args.index("into")+1], args[args.index("format") +1:])
elif args[0] == 'create':
    #create table rows()
    Commands.create(args[1:])
elif args[0] == 'delete':
    Commands.delete(args[1])
elif args[0] == "remove": 
    Commands.remove(args[1], args[args.index("where")+1:])
elif args[0] == "help" :
    print("INSERT ::: Insert ROW VALUES INTO TABLE_NAME FORMAT COLUMN_FORMAT  ")
    print("SELECT ::: SELECT ROW VALUES FROM TABLE_NAME WHERE CONDITIONAL")
    print("REMOVE :::  REMOVE TABLE_NAME WHERE CONDITIONAL ")
    print("DELETE :::  DELETE TABLE_NAME")


