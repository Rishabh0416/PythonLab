##Insurance varification ,checking on basis of Marital status, Sex, Age.

#input Marital status
mstat=input('Enter marital status: ')

#input sex
s=input('Enter sex: ')

#input age
age=int(input('Enter age: '))

#conditions
if (mstat=='m') or (mstat=='u'and s=='m' and age > 30)\
    or (mstat=='u' and s=='f' and age > 25):
    print('Insured')
else:
    print('Not insured')
