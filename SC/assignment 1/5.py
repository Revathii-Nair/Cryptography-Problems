A = {'x1': 0.2, 'x2': 0.5, 'x3': 0.8}
B = {'y1': 0.4, 'y2': 0.7, 'y3': 0.3}
C = {'y1': 0.6, 'y2': 0.2, 'y3': 0.9}

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