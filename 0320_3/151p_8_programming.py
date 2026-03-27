weight, height = eval(input("체중과 키를 입력하시오: "))
std_weight = (height - 100) * 0.9
if weight > std_weight:
    print("과체중입니다.")
elif weight == std_weight:
    print("표준체중입니다.")
else:
    print("저체중입니다.")