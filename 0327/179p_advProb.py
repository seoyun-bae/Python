import random

tries = 0
guess = 0
answer = random.randint(1, 100)

print("1부터 100 사이의 숫자를 맞추시오")

while guess != answer and tries < 10 :
    guess = int(input("숫자를 입력하시오: "))
    tries = tries + 1
    if guess < answer :
        print("낮아요")
    elif guess > answer :
        print("높아요")

if guess == answer :
    print("정답이에요~ 시도횟수: ", tries)
else :
    print("10번안에 못맞췄어요 아쉬워요 ㅠㅠ 정답은", answer)