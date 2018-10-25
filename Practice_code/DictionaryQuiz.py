names_nicknames = {"David" : "Güero" , "Santiago" : "Cabezon"}
names_nicknames["Deleon"] = "Cholo"
names_nicknames["Camacho"] = "Indio"
names_nicknames["Moore"] = " Zombie" 
description= ""
for x in names_nicknames:
    description += x + " goes by the name " +names_nicknames[x] + ", "
print(description)