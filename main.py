#main
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




#Project2
## Writing code to get required results on the string "Bamboozled".
s='Bamboozled'

# extract B a
print(s[0], s[1])
print(s[-10], s[-9])

#extract e d
print(s[8], s[9])
print(s[-2], s[-1])

#extract mboozled
print(s[2:10])
print(s[2:])
print(s[-8:])

#extract Bamboo
print(s[0:6])
print(s[:6])
print(s[-10:-4])
print(s[:-4])

#reverse Bamboozled
print(s[::-1])


print(s[0:10:1])
print(s[0:10:2])
print(s[0:10:3])
print(s[0:10:4])

s= s+'Hype!'
print(s)
s=s[:6] + 'Monger' +s[-1]
print(s)