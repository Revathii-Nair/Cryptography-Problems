
def caesar(text):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + 3) % 26 + base)
        else:
            result += ch
    return result

def modified_caesar(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + key ) % 26 + base)
        else:
            result += ch
    return result


def make_matrix(key):
    key = key.upper().replace("J", "I")
    letters = ""
    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in letters:
            letters += ch
    return [list(letters[i:i + 5]) for i in range(0, 25, 5)]

def find(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c

def playfair(text, key):
    matrix = make_matrix(key)
    text = "".join(c for c in text.upper().replace("J", "I") if c.isalpha())
    pairs, i = [], 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"
        if a == b:
            b = "X"
            i += 1
        else:
            i += 2
        pairs.append((a, b))

    result = ""
    for a, b in pairs:
        r1, c1 = find(matrix, a)
        r2, c2 = find(matrix, b)
        if r1 == r2:                    
            result += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:              
            result += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:                           
            result += matrix[r1][c2] + matrix[r2][c1]
    return result


text = input("Enter text: ")
print("\n--- Caesar Cipher ---")
print("Encrypted:", caesar(text))

print("\n--- Modified Caesar Cipher ---")
k = int(input("Enter key (number): "))
print("Encrypted:", modified_caesar(text, k))

print("\n--- Playfair Cipher ---")
pk = input("Enter keyword: ")
print("Encrypted:", playfair(text, pk))