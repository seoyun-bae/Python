import random

computer_choice = random.randint(1, 3)
user_choice = int(input("어디를 수비하시겠어요?(왼쪽: 1, 중앙: 2, 오른쪽: 3): "))

if user_choice < 1 or user_choice > 3:
    print("잘못된 입력입니다. 1, 2, 3 중에서 선택해야 합니다.")
else:
    if computer_choice == user_choice:
        print("수비에 성공하셨습니다.")
    else:
        print("페널티킥이 성공하였습니다.")