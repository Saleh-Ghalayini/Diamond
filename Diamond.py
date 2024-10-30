#asking user to input nb of rows
rows_number = int(input("please enter the number of rows you want to print for your diamond shape: "))

print(f"For rows = {rows_number}")

#working on the top half of the shape where the nb of spaces is decreasing and the nb of "*" is increasing according to the formulas written below
for i in range(rows_number):
    for j in range(rows_number - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
#working on the bottom half of the shape where the nb of spaces is increasing and the nb of "*" is decreasing according to the formulas written below
#keeping in mind that the bottom half has 1 less row than the top half
for i in range(1, rows_number):
    for j in range(rows_number + i - rows_number):
        print(" ", end="")
    for k in range((rows_number - i) * 2 - 1):
        print("*", end="") 
    print()