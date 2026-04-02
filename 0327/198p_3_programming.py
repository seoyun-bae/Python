total = 0
for i in range(1, 101):
    if i % 3 == 0:
        total += i

print("1 부터 100 사이의 모든 3의 배수의 합은", total, "입니다.")