address = input("이메일 주소를 입력하시오: ")

parts = address.split(".")

print(f"입력된 주소: {address}")
print(f"\".\"을 기준으로 분리된 결과(리스트): {parts}")


for i in range(len(parts)):
    print(f"{i+1}번째 부분: {parts[i]}")