
A = {'x1': 0.2, 'x2': 0.7, 'x3': 0.5}
B = {'x1': 0.6, 'x2': 0.4, 'x3': 0.8}

union = {}
intersection = {}
complementA = {}

for key in A:
    union[key] = max(A[key], B[key])
    intersection[key] = min(A[key], B[key])
    complementA[key] = 1 - A[key]

print("Union:", union)
print("Intersection:", intersection)
print("Complement of A:", complementA)