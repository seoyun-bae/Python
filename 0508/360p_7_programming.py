calendar = {}

for _ in range(2):
    date = input("날짜를 입력하시오: ")
    job = input("일정을 입력하시오: ")
    if date not in calendar:
        calendar[date] = []
    calendar[date].append(job)