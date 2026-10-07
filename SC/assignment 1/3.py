# A = {'x1': 0.2, 'x2': 0.5, 'x3': 1}
# B = {'y1': 0.3, 'y2': 0.8}

A={}
B={}

n = int(input("Enter number of elements in A: "))
for i in range(n):
    key =input("Enter term: ")
    A[key] =float(input("Enter value in A: "))

n =int(input("Enter number of elements in B: "))
for i in range(n):
    key =input("Enter term: ")
    B[key] =float(input("Enter value in B: "))

product=[]
for x in A:
    row=[]
    for y in B:
        row.append(min(A[x],B[y]))
    product.append(row)

print("Cartesian Product of A and B:")
for x in product:
    for y in x:
        print(y,end=" ")