#Project 9.
##program to show-How to merge two dictionaries
##creating two separate dictionaries namely,'boys','girls'.
boys={'Nilesh':41,'Soumitra':42,'Nadeem':47}
girls={'Rasika':38,'Rajashree':43,'Rasika':45}

## Now combining
combined={**boys,**girls}
print(combined)
combined={**girls,**boys}
print(combined)