#List operations

#creating list of 5 names
names=['rishabh','rk','nikki','divyanshu','sayam']
print(names)

#insert a name 'atharva' before 'nikki'
names.insert(2,'atharva')
print(names)

#append name 'kamla'
names.append('kamla')
print(names)
#delete 'sayam' from list
names.remove('sayam')
print(names)

#replace 'rishabh' with 'rishabh singh'
i=names.index('rishabh')
names[i]='rishabh singh'
print(names)

#sort all the names in the list
names.sort()
print(names)

#print reverse sorted list
names.reverse()
print(names)