A={}
B={}
C={}

n = int(input("Enter number of elements in A: "))
for i in range(n):
    key = input("Enter term: ")
    A[key] = float(input("Enter value in A: "))

n = int(input("Enter number of elements in B: "))
for i in range(n):
    key = input("Enter term: ")
    B[key] = float(input("Enter value in B: "))

n = int(input("Enter number of elements in C: "))
for i in range(n):
    key = input("Enter term: ")
    C[key] = float(input("Enter value in C: "))

A_complement = {}
for x in A:
    A_complement[x] = round(1 - A[x], 2)

AB = []

for x in A:
    row = []
    for y in B:
        row.append(min(A[x], B[y]))
    AB.append(row)

print("AxB:")
for row in AB:
    print(row)


A_C = []
for x in A:
    row = []
    for y in C:
        row.append(min(A_complement[x], C[y]))
    A_C.append(row)

print("A'xC:")
for row in A_C:
    print(row)


result = []
for i in range(len(AB)):
    row = []
    for j in range(len(AB[i])):
        row.append(max(AB[i][j], A_C[i][j]))
    result.append(row)

print("\nIF A THEN B ELSE C = (A x B) U (A' x C):")
for row in result:
    print(row)