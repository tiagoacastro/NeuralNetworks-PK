x = input()
x = input()
x = float(x)

if x % 2 == 0:
    x *= 3
elif x > 10:
    x += 3
else:
    x += 1

print(x)