'''
set - cannot contain duplicates and item's can't be changed(just add\delete)
tuple - ordered and can't be cnanged, can contain duplicates'
list - can contain duplicates and item of list can be changed directly
'''
try:
    userInp = int(input('Please enter your N: '))
except:
    print('Error, run program again.')

if userInp % 2 == 0:
    for i in range(0, userInp + 1, 2):
        print(str("*" * i).center(30))              #in case %2 = 0
    for i in range(userInp - 2, 0, -2):             #ex. 2,4,6,8,10 etc
        print(str("*" * i).center(30))
else:
    for i in range(1, userInp + 1, 2):
        print(str("*" * i).center(30))              #in case %2 !=0
    for i in range(userInp - 2, 0, -2):             #ex. 1,3,5,7,9 etx
        print(str("*" * i).center(30))
