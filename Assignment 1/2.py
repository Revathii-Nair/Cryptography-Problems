
def rail_fence(text, rails):
    fence = [""] * rails
    row, step = 0, 1
    for ch in text:
        fence[row] += ch
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step
    return "".join(fence)


def columnar(text, key):
    text = text.replace(" ", "")

    while len(text) % len(key) != 0:
        text += "X"

    result = ""

    for ch in sorted(key):
        col = key.index(ch)
        for i in range(col, len(text), len(key)):
          result += text[i]

    return result

text = input("Enter text: ")

print("\n--- Rail Fence ---")
n = int(input("Enter key: "))
print("Encrypted:", rail_fence(text.replace(" ", ""), n))

print("\n--- Columnar Transposition ---")
key = input("Enter key word: ").upper()
print("Encrypted:", columnar(text.upper(), key))