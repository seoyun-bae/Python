weight = float(input("몸무게를 kg 단위로 입력하시오:"))
height1 = float(input("키를 cm 단위로 입력하시오:"))
height2 = height1 / 100
bmi = (weight / (height2**2))
print("당신의 BMI=", bmi)