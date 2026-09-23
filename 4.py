A = [0.2, 0.6, 0.8]
B = [0.3, 0.7, 0.5]

relation = []

for a in A:
    row = []
    for b in B:
        row.append(min(a, b))
    relation.append(row)

print("IF A THEN B Relation")

for row in relation:
    print(row)