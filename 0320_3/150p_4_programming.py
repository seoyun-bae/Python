radius = int(input("원의 반지름: "))

if radius < 0:
    print("잘못된 값입니다.")
else:
    area = 3.14*radius**2
    print("원의 면적:", area)