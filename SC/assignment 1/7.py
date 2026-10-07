n = int(input("Enter matrix size: "))
R = []
print("Enter the matrix:")
for i in range(n):
    row = []
    for j in range(n):
        value = float(input())
        row.append(value)
    R.append(row)

alpha = float(input("Enter alpha value: "))
cut = []

print("\nAlpha-Cut Matrix:")
for i in range(n):
    row = []
    for j in range(n):
        if R[i][j] >= alpha:
            row.append(1)
        else:
            row.append(0)
    cut.append(row)
    print(row)


