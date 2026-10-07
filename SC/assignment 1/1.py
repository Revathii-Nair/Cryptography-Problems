n = int(input("Enter number of elements: "))

A ={}
B ={}

print("\nEnter terms and values for Set A and Set B:")

for i in range(n):
    key = input("Enter term: ")
    A[key] =float(input("Enter value in A: "))
    B[key] =float(input("Enter value in B: "))

union = {}
intersection = {}
complementA = {}

for key in A:
    union[key] = max(A[key], B[key])
    intersection[key] = min(A[key], B[key])
    complementA[key] = 1 - A[key]

print("\nSet A:", A)
print("Set B:", B)

print("\nUnion:", union)
print("Intersection:", intersection)
print("Complement of A:", complementA)