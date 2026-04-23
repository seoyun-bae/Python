def getSorted(x, y):
    if x > y:
        return y, x
    return x, y

a = int(input("첫 번째 정수: "))
b = int(input("두 번째 정수: "))
print(getSorted(a, b))