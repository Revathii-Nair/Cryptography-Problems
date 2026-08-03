# Playfair Cipher Encryption (no defs)

plaintext = input("Enter the plain text: ")
keyword = input("Enter the keyword: ")

# --- Create 5x5 matrix ---
keyword = keyword.upper().replace("J", "I")
matrix_chars = []
for ch in keyword:
    if ch.isalpha() and ch not in matrix_chars:
        matrix_chars.append(ch)
for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # no J
    if ch not in matrix_chars:
        matrix_chars.append(ch)
matrix = [matrix_chars[i*5:(i+1)*5] for i in range(5)]

print("\nKeyword Matrix:")
for row in matrix:
    print(" ".join(row))
print()

# --- Prepare plaintext ---
text = plaintext.upper().replace("J", "I")
text = "".join(ch for ch in text if ch.isalpha())
prepared = []
i = 0
while i < len(text):
    a = text[i]
    if i + 1 < len(text):
        b = text[i+1]
        if a == b:
            prepared.append(a)
            prepared.append('X')
            i += 1
        else:
            prepared.append(a)
            prepared.append(b)
            i += 2
    else:
        prepared.append(a)
        prepared.append('X')
        i += 1

print("Prepared Plaintext (digraphs):", " ".join(
    "".join(prepared[i:i+2]) for i in range(0, len(prepared), 2)
))

# --- Encrypt ---
ciphertext = ""
for i in range(0, len(prepared), 2):
    a, b = prepared[i], prepared[i+1]

    # find positions
    ra = rb = ca = cb = None
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == a:
                ra, ca = r, c
            if matrix[r][c] == b:
                rb, cb = r, c

    if ra == rb:  # same row
        ciphertext += matrix[ra][(ca+1) % 5] + matrix[rb][(cb+1) % 5]
    elif ca == cb:  # same column
        ciphertext += matrix[(ra+1) % 5][ca] + matrix[(rb+1) % 5][cb]
    else:  # rectangle
        ciphertext += matrix[ra][cb] + matrix[rb][ca]

print("\nOriginal Plain Text  :", plaintext)
print("Cipher Text          :", ciphertext)
