n = int(input("입력할 값의 개수: "))

values = []

for _ in range(n):
    num = int(input())
    values.append(num)
total = sum(values)
print(f"값의 합계 = {total}")