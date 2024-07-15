price = 1000000
good_cred = False
if good_cred:
    print("Put 10%")
    payment = (0.10*price)
else:
    print('Put 20%')
    payment = (0.20*price)

print('Down payment: $', payment)
