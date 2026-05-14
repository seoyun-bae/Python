message = input("트위터 메시지를 입력하시오: ")

upper_count = 0

for char in message:
    if char.isupper():  
        upper_count += 1

print(f"대문자의 개수: {upper_count}")