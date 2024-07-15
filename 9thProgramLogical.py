name = input('Enter your name: ')

if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 10:
    print('name can be maximum of 10 characters')
else:
    print('Looks good!')