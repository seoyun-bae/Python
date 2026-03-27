x, y, z = eval(input("3개의 정수를 입력하시오: "))
if x < y:
    min_val = x
else:
    min_val = y
if z < min_val:
    min_val = z
print("제일 작은 정수는", min_val, "입니다.")
