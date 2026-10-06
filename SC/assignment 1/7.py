R = [
    [1,0.7,0.4,0.4],
    [0.7,1,0.4,0.4],
    [0.4,0.4,1,0.5],
    [0.4,0.4,0.5,1]
]
alpha = 0.7
n = len(R)

cut = []
print("Alpha-Cut Matrix:")
for i in range(n):
    row = []
    for j in range(n):
        if R[i][j] >= alpha:
            row.append(1)
        else:
            row.append(0)
    cut.append(row)
    print(row)


seen = []
print("\nR" + str(alpha) + "=", end=" ")
for i in range(n):
    if cut[i] in seen:
        continue
    if len(seen) > 0:
        print(",", end="")
    seen.append(cut[i])
    group = []
    for j in range(n):
        if cut[i] == cut[j]:
            group.append("x" + str(j + 1))
    print("{" + ",".join(group) + "}", end="")
print()

