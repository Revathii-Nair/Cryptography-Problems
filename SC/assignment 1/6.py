R = [
    [0.1, 0.6, 1]
]

S = [
    [1, 0.6, 0.3],
    [0.5, 0.5, 0.3],
    [0.2, 0.2, 0.2]
]

print("Relation R:")
for row in R:
    print(row)

print("\nRelation S:")
for row in S:
    print(row)

maxmin = []
maxprod = []

for i in range(len(R)):
    row = []
    for j in range(len(S[0])):
        maxv = 0
        for k in range(len(S)):
            minv = min(R[i][k], S[k][j])
            if minv > maxv:
                maxv = minv
        row.append(maxv)
    maxmin.append(row)

for i in range(len(R)):
    row = []
    for j in range(len(S[0])):
        maxv = 0
        for k in range(len(S)):
            product = R[i][k] * S[k][j]
            if product > maxv:
                maxv = product
        row.append(maxv)
    maxprod.append(row)

print("\nMax-Min Composition (R o S):")
for row in maxmin:
    print(row)

print("\nMax-Prod Composition (R o S):")
for row in maxprod:
    print(row)