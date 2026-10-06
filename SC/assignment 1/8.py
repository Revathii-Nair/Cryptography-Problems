high = [0, 0.2, 0.4, 0.7, 1.0]
low = [1, 0.8, 0.6, 0.4, 0.2]

print("Base terms : high, low")
print("Hedges: very, fairly, slightly")
words = input("Enter term (e.g. very very high): ").lower().split()

last = words[-1]
if last != "high" and last != "low":
    print("Unknown base term:", last)
    exit()

power = 1
for i in range(len(words) - 1):
    if words[i] == "very":
        power = power * 2
    elif words[i] == "fairly":
        power = power * (2 / 3)
    elif words[i] == "slightly":
        power = power * 0.5
    else:
        print("Unknown hedge:", words[i])
        exit()

print("\nResult:")
for j in range(5):
    if last == "high":
        value = high[j]
    else:
        value = low[j]
    result = value ** power
    print(f"{result:.4f}", end=" ")
print()