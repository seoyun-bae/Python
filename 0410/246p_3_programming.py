def calc(a, b):
    return a+b, a-b, a*b, a/b

x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번째 정수를 입력하시오: "))

res1, res2, res3, res4 = calc(x, y)
print(f"{res1}, {res2}, {res3}, {res4}이 반환되었습니다.")