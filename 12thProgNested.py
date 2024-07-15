#PRINTING CHECKER BOARD USING NESTED LOOP
rows, column = range(0, 8), range(0, 8)
for row in rows:
    for col in column:
        if (row + col) % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()
