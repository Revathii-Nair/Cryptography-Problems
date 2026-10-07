high = [0, 0.2, 0.4, 0.7, 1.0]
low = [1, 0.8, 0.6, 0.4, 0.2]

print("Linguistic terms: high, low")
print("Hedges: very, fairly, slightly, not")
print("Operators: and, or")
words = input("Enter term: ").lower().split()

def evaluate(words):
    last = words[-1]
    if last == "high":
        values = high[:]
    elif last == "low":
        values = low[:]
    else:
        print("Unknown term:", last)
        exit()
    
    power = 1
    negate = False
    for word in words[:-1]:
        if word == "very":
            power *= 2
        elif word == "fairly":
            power *= (2 / 3)
        elif word == "slightly":
            power *= 0.5
        elif word == "not":
            negate = not negate
        else:
            print("Unknown hedge:", word)
            exit()
    
    result = []
    for value in values:
        result.append(value ** power)

    if negate:
        temp = []
        for value in result:
            temp.append(1 - value)
        result = temp

    return result


if "or" in words:
    pos = words.index("or")
    left = evaluate(words[:pos])
    right = evaluate(words[pos + 1:])
    result = []
    for i in range(len(left)):
        result.append(max(left[i], right[i]))

elif "and" in words:
    pos = words.index("and")
    left = evaluate(words[:pos])
    right = evaluate(words[pos + 1:])
    result = []
    for i in range(len(left)):
        result.append(min(left[i], right[i]))

else:
    result = evaluate(words)

print("\nResult:")
for value in result:
    print(f"{value:.4f}", end=" ")

print()
