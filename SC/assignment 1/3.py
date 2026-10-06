A = {'a': 0.2, 'b': 0.8}
B = {'x': 0.5, 'y': 0.9}

print("Cartesian Product:")

for i in A:
    for j in B:
        value = min(A[i], B[j])
        print((i, j), "=", value)