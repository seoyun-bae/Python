def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번째 정수를 입력하시오: "))

print(f"({x} + {y}) = {add(x, y)}")
print(f"({x} - {y}) = {sub(x, y)}")
print(f"({x} * {y}) = {mul(x, y)}")
print(f"({x} / {y}) = {div(x, y)}")