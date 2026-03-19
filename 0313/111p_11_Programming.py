drive = input("드라이브 이름: ")
directory = input("디렉토리 이름: ")
filename = input("파일 이름: ")
extension = input("확장자: ")

full = drive + ":" + directory + filename + "." + extension

print("완전한 이름은", full)