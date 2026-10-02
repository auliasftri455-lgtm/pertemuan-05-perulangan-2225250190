n = int(input("N: "))
total = 0

for i in range(2, n + 1, 2):
    total += i

print("Jumlah genap =", total)