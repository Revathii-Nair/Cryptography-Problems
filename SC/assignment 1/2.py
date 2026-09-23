A = {'x1': 0.2, 'x2': 0.7, 'x3': 0.5}
B = {'x1': 0.6, 'x2': 0.4, 'x3': 0.8}

left1 = {}
right1 = {}

for x in A:
    left1[x] = 1 - max(A[x], B[x])
    right1[x] = min(1 - A[x], 1 - B[x])

print("(A U B)' =", left1)
print("A' ∩ B' =", right1)

left2 = {}
right2 = {}

for x in A:
    left2[x] = 1 - min(A[x], B[x])
    right2[x] = max(1 - A[x], 1 - B[x])

print("(A ∩ B)' =", left2)
print("A' U B' =", right2)