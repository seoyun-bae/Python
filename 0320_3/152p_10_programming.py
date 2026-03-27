x = float(input("x의 값을 입력하시오: "))

if x <= 0:
    result = x**2 - 9*x + 2
else:
    result = 7*x + 2

print(f"f(x)의 값은 {result:.6f}")