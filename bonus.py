'''
set - cannot contain duplicates and item's can't be changed(just add\delete)
tuple - ordered and can't be cnanged, can contain duplicates'
list - can contain duplicates and item of list can be changed directly
'''
try:
    userInp = int(input('Please enter your N: '))
except:
    print('Error, run program again.')

for i in range(1,userInp+1,2):
    print(str("*"*i).center(30))
for i in range(userInp-1,0,-2):
    print(str("*"*i).center(30))

