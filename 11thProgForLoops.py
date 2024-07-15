#MULTIPLICATION TABLE USING FOR LOOP
for nums in range(1, 11):
    for n in range(1, 11):
        multi = nums * n
        if n == 1:
            print("=" * 5, 'Multiplication Table No. ', nums, "=" * 5)
        print(f"\t\t\t{nums} x {n} = {multi}")
#PRINT EVEN NUMBERS
lamaw = 0
while lamaw <= 100:
    print(lamaw, end=" ")
    lamaw += 2
#PRINT EVEN NUMBERS BACKWARDS
print("\n")
wamal = 100
while wamal >= 0:
    print(wamal, end=" ")
    wamal -= 2
print("\n")
#PRINT ODD NUMBERS
xD = 1
while xD <= 101:
    print(xD, end=" ")
    xD += 2
