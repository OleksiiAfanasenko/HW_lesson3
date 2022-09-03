Eleks = ["Oleksii", "Maksim", "Viktor"]
Toshiba = ["Oleksii", "Andrii", "Ruslan"]
Toshiba.extend(Eleks)
print(Toshiba)

casino_blacklist = ['John Dow', 'John_Smith', 'John Lin', 'John Gol']
poker_blacklist = ['John Dow', 'John Dic', 'John Bim', 'John Bol']
alcohol_blacklist = ['John Dow', 'John Uil', 'John Won', 'John Pol']
casino_blacklist.extend(poker_blacklist)
casino_blacklist.extend(alcohol_blacklist)
print(casino_blacklist.count('John Dow'))
#не впевнен що вірно, бо якщо масив даних великий то дуже муторно шукати по одній людині, а список я не зміг вставити

group_one = {"vegetables": "omnivores1",
             "all": "omnivores2",
            }
group_two = {"vegetables": "vegetarian",
            }
print(group_one.get("vegetables"))
print(group_two.get("vegetables"))

