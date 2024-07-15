numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
maz = numbers[0]
for it in numbers:
    if it > maz:
        maz = it
print(maz)

for mini in reversed(numbers):
    if mini < maz:
        maz = mini
print(maz)
