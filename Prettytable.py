from prettytable import PrettyTable

table = PrettyTable()

table.add_column("City",["Mumbai","Vijayawada","Chennai","Noida"])
table.add_column("State",["Maharashtra","Andhra Pradesh","Tamilnadu","Uttar Pradesh"])
table.add_column("Language",["Maratha","Telugu","Tamil","Hindi"])
table.align = 'l'
print(table)