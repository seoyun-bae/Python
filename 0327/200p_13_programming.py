n = int(input("몇 번째 항을 구할까요? "))
f0, f1 = 0, 1

for i in range(n):
    print(f0, end=" ")
    f0, f1 = f1, f0 + f1
