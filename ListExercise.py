#write a program that removes duplicated list
numbers = [1, 1, 2, 3, 4, 2, 3, 4, 5]
uni = []
for num in numbers:
    if num not in uni:
        uni.append(num)
print(uni)
