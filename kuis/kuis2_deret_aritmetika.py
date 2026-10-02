a = int(input("Suku pertama (a): "))
d = int(input("Beda (d): "))
n = int(input("Banyak suku (n): "))

total = 0

for i in range(n):
    suku = a + i * d
    print(suku, end=" ")
    total += suku

print()
print("Jumlah =", total)