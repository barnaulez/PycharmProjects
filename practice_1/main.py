from prettytable import PrettyTable

table = PrettyTable()
table.add_column("City", ["Moscow", "St. Petersbourg", "Novosibirsk", "Ekaterinburg", "Kazan", "Barnaul"])
table.add_column("Population, K Ppl", [12632, 5377, 1620, 1492, 1257, 631])
table.align["City"] = "l"
table.align["Population"] = "c"
print(table)
