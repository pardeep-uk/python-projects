from prettytable import *

table = PrettyTable()


table.add_column("Pokemon Name",["Pickachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align["Pokemon Name"] = "r"
table.align["Type"] ='r'

print(table)


