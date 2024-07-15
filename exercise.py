weight = float(input('Enter your weight: '))
chooser = input('(L)bs or (K)g: ')
if chooser.upper() == 'K':
    mass = weight * 2.205
    print(f"you are {mass} pounds")
else:
    mass = weight / 2.205
    print(f"you are {mass} kilos")
