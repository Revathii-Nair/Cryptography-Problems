A = {'x1': 0.2, 'x2': 0.5, 'x3': 0.8}
B = {'y1': 0.4, 'y2': 0.7, 'y3': 0.3}
Y = {'y1': 1, 'y2': 1, 'y3': 1}

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