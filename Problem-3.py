a = int(input("Enter a: "))


if a % 2 == 0:
    last_odd = a - 1
else:
    last_odd = a

result = list(range(1, last_odd + 1, 2))

print(", ".join(map(str, result)))
