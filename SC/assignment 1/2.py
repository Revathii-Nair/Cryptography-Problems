n = int(input("Enter number of elements: "))

A = {}
B = {}

print("\nEnter terms and values for Set A and Set B:")

for i in range(n):
    key = input("Enter term: ")
    A[key] = float(input("Enter value in A: "))
    B[key] = float(input("Enter value in B: "))

left1 = {}
right1 = {}

for x in A:
    left1[x] = 1 - max(A[x], B[x])
    right1[x] = min(1 - A[x], 1 - B[x])

print("(A u B)' =", left1)
print("A' ∩ B' =", right1)

left2 = {}
right2 = {}

for x in A:
    left2[x] = 1 - min(A[x], B[x])
    right2[x] = max(1 - A[x], 1 - B[x])

print("(A ∩ B)' =", left2)
print("A' U B' =", right2)