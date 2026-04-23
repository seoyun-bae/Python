import random

def dice_game():
    print("========== dice_game() 호출 ==========")
    human = random.randint(1, 6)
    com = random.randint(1, 6)
    
    print(f"인간: 주사위값= {human}")
    print(f"컴퓨터: 주사위값= {com}")
    
    if human > com: print("인간승리")
    elif human < com: print("컴퓨터승리")
    else: print("무승부")
    print("========== dice_game() 복귀 ==========")

while True:
    dice_game()
    choice = input("\n중단할까요? Y/N: ")
    if choice.upper() == 'Y':
        break