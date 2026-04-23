def checkPass(p):
    has_upper = any(c.isupper() for c in p)
    has_lower = any(c.islower() for c in p)
    has_digit = any(c.isdigit() for c in p)
    
    if len(p) >= 8 and has_upper and has_lower and has_digit:
        return True
    return False

while True:
    pw = input("패스워드를 입력하시오: ")
    if checkPass(pw):
        print("사용할 수 있습니다.")
        break
    else:
        print("사용할 수 없습니다. 다시 입력하세요!")