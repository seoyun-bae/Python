def main():
    address_book = {} 
    while True :
        user = display_menu();
        if user == 1 :
            name, number = get_contact()
            address_book[name] = number # name과 number를 추가한다.
        elif user == 2 :
            name = input("삭제할 이름을 입력하시오: ")
            if name in address_book:
                address_book.pop(name)
                print(f"{name}님의 연락처가 삭제되었습니다.")
            else:
                print(f"{name}님의 연락처를 찾을 수 없습니다.")
        elif user == 3 :
            name = input("검색할 이름을 입력하시오: ")
            if name in address_book:
                print(f"{name}의 전화번호: {address_book[name]}")
            else:
                print(f"{name}님의 연락처가 존재하지 않습니다.")
        elif user == 4 :
            for key in sorted(address_book):
                print(key, "의 전화번호:", address_book[key])
        elif user == 5 :
            print("프로그램을 종료합니다.")
            break
        else :
            print("잘못된 메뉴 선택입니다.")

def get_contact():
    name = input("이름: ")
    number = input("전화번호: ")
    return name, number 


def display_menu() :
    print("\n1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    select = int(input("메뉴 항목을 선택하시오: "))
    return select

main()