seats = [[0] * 10 for _ in range(10)]

while True:
    print("--------------------")
    print("  1 2 3 4 5 6 7 8 9 10")
    print("--------------------")
    for row in seats:
        print(" ".join(map(str, row)))
        
    r = int(input("원하시는 좌석의 행번호(종료 -1): "))
    if r == -1: break
    c = int(input("원하시는 좌석의 열번호(종료 -1): "))
    if c == -1: break
    
    if seats[r-1][c-1] == 0:
        seats[r-1][c-1] = 1
        print("예약되었습니다.")
    else:
        print("이미 예약된 좌석입니다.")