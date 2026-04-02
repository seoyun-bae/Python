username = ""
password = ""

while username != "express" or password != "python" :
    username = input("아이디를 입력하시오: ")
    password = input("암호를 입력하시오: ")

    if username != "express" or password != "python" :
        print("아이디 또는 암호가 틀렸습니다. 다시 입력하세요.")

print("로그인 성공")