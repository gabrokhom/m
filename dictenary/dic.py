my_dict={
    'name':'Gabriel',
    'age': 14,
    'surname':'Khomasuridze',
    'weight': 45,
    'hobby': 'chess'
}
print(my_dict)

for i in my_dict:
    print(i)

for i in my_dict.values():
    print(i)

for i in my_dict.items():
    print(i)


#accsesing items
print(my_dict['weight'])

#adding items 
my_dict['schoolname']='vcl'
print(my_dict)

#updating items
my_dict['weight']=46
print(my_dict)

#deliting items
# my_dict.pop('schoolname')
# print(my_dict)

del my_dict['schoolname']
print(my_dict)

if 'schoolname' in my_dict:
    print('yes')

else:
    print('no')