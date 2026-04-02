a = int(input("첫 번째 정수를 입력하시오: "))
b = int(input("두 번째 정수를 입력하시오: "))

for i in range(min(a,b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(f"{a}와 {b}의 최대공약수는 {i}입니다.")
        break
