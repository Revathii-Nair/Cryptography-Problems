A = {}
B = {}
Y = {}

n = int(input("Enter number of elements in A: "))
for i in range(n):
    key = input("Enter term: ")
    A[key] = float(input("Enter value in A: "))

n = int(input("Enter number of elements in B: "))
for i in range(n):
    key = input("Enter term: ")
    B[key] = float(input("Enter value in B: "))

for i in range(A):
    Y["y" + str(i + 1)] = 1

A_comp = {}
for x in A:
    A_comp[x] = round(1 - A[x], 2)


AB = []
A_Y = []

for x in A:
    row = []
    for y in B:
        row.append(min(A[x], B[y]))
    AB.append(row)

print("AxB:")
for row in AB:
    print(row)

for x in A:
    row = []
    for y in Y:
        row.append(min(A_comp[x], Y[y]))
    A_Y.append(row)

print("\nA'xY:")
for row in A_Y:
    print(row)


result = []

for i in range(len(AB)):
    row = []
    for j in range(len(AB[i])):
        row.append(max(AB[i][j], A_Y[i][j]))
    result.append(row)

print("\nIF A THEN B = (A x B) U (A' x Y):")
for row in result:
    print(row)