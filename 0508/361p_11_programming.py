problems = {"파이썬": "최근에 가장 떠오르는 프로그래밍 언어"}
for ans, desc in problems.items():
    print(f"다음은 어떤 단어에 대한 설명일까요?")
    print(f'"{desc}"')
    print("(1)파이썬 (2)변수 (3)함수 (4)리스트")
    guess = input()
    if guess == ans:
        print("정답입니다. !")