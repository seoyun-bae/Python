s = input("문자열을 입력하시오: ")


reversed_s = ""


for char in s:
    reversed_s = char + reversed_s 

if s == reversed_s:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")