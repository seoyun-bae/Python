n = int(input("n의 값을 입력하세요: "))
result = 0

for i in range(1, n + 1):
    result += i**2

print(f"계산값은 {result}입니다.")
