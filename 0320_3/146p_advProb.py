a = int(input("삼각형의 한 변을 입력하시오: "))
b = int(input("삼각형의 한 변을 입력하시오: "))
c = int(input("삼각형의 한 변을 입력하시오: "))

if (a + b) > c and (b + c) > a and (a + c) > b:
    print("올바른 삼각형")
    
    angle1 = int(input("삼각형의 첫 번째 내각을 입력하시오: "))
    angle2 = int(input("삼각형의 두 번째 내각을 입력하시오: "))
    angle3 = int(input("삼각형의 세 번째 내각을 입력하시오: "))

    if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3) == 180:
        print("내각의 합이 180도이므로 올바른 삼각형입니다.")
    else:
        print("내각의 합이 180도가 아니므로 올바르지 않은 삼각형입니다.")

else:
    print("올바르지 않은 삼각형")
    