def getIntRange(a, b, msg):
    while True:
        v = int(input(msg))
        if a <= v <= b:
            return v

month = getIntRange(1, 12, "월을 입력하시오(1부터 12사이의 값): ")
day = getIntRange(1, 31, "일을 입력하시오(1부터 31사이의 값): ")
print(f"입력된 날짜는 {month}월 {day}일입니다.")