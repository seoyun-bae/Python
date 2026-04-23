board = [[' ' for x in range(3)] for y in range(3)]

while True:
    for r in range(3):
        print(" " + board[r][0] + " | " + board[r][1] + " | " + board[r][2])
        if (r != 2):
            print("---+---+---")
            
    x = int(input("다음 수의 x좌표를 입력하시오: "))
    y = int(input("다음 수의 y좌표를 입력하시오: "))

    if board[x][y] != ' ':
        print("잘못된 위치입니다.")
        continue
    else:
        board[x][y] = 'X'
    
    done = False
    for r in range(3):
        for j in range(3):
            if board[r][j] == ' ' and not done:
                board[r][j] = 'O'
                done = True
                break