loop_count = int(input("반복 횟수를 입력하세요: "))
pi = 3.0
n = 2
sign = 1
for i in range(loop_count):
    term = 4.0 / (n * (n + 1) * (n + 2))
    pi = pi + (sign*term)
    n += 2
    sign *= -1

print(f"Pi = {pi:.15f}")