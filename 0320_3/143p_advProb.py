print("======================")
print("메뉴 1번: 치즈 버거")
print("메뉴 2번: 치킨 버거")
print("메뉴 3번: 불고기 버거")
print("======================")

print("======================")
print("음료 4번: 콜라")
print("음료 5번: 환타파인")
print("음료 6번: 스프라이트")
print("======================")

selection = int(input("메뉴를 선택하세요: "))

if selection >=1 and selection <=3 :
    print("메뉴 ", selection)
else:
    print("잘못 입력하셨습니다.")
selection = int(input("음료를 선택하세요: "))

if selection >=4 and selection <=6 :
    print("음료 ", selection)
else:
    print("잘못 입력하셨습니다.")
