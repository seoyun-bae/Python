def menu():
    print("1. 섭씨 온도->화씨 온도")
    print("2. 화씨 온도->섭씨 온도")
    print("3. 종료")
    select = int(input("메뉴를 선택하세요: "))
    return select

def ctof(c):
    temp = c * 9 / 5 + 32
    return temp

def ftoc(f):
    temp = (f - 32) * 5 / 9
    return temp

def input_f():
    f = float(input("화씨 온도를 입력하세요: "))
    return f

def input_c():
    c = float(input("섭씨 온도를 입력하세요: "))
    return c

def main():
    while True:
        index = menu()
        if index == 1:
            t = input_c()
            t2 = ctof(t)
            print("화씨 온도: ", t2, "\n")
        elif index == 2:
            f = input_f()
            t2 = ftoc(f)
            print("섭씨 온도: ", t2, "\n")
        else:
            break

main()