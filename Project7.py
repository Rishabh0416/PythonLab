#Tuple functions

tpl=('F','l','a','b','b','e','r','g','a','s','t','e','d')

#adding '!' to tuple
#Impossible as tuple is immutable
#Therefore creating a new tuple and making 'tpl' refer to it.
tpl= tpl+('!',)
print(tpl)

#converting tuple to string
str = ''.join(tpl)
print(str)

#extracting ('b','b') from tuple
t=tpl[3:5]
print(t)

#counting number of 'e' in the tuple
count=tpl.count('e')
print('count=',count)

#checking whether 'r' exists in the tuple or not.
print('r' in tpl)

#converting tuple to a list
list=list(tpl)
print(list)

#removing 'b','b','e','r' from the tuple
#tuple are immutable, hence not possible
#so, we split the tuple, remove the unwanted elements, then merge the tuples.
tpl=tpl[:3]+tpl[7:]
print(tpl)
