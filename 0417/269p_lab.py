menu = 0
friends = []
while menu != 9 :
    print("---------------")
    print("1. 친구리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    menu = int(input("메뉴를 선택하시오: "))
    if menu == 1 :
        print(friends)
    elif menu == 2 :
        name = input("이름을 입력하시오: ")
        friends.append(name)
    elif menu == 3 :
        name2 = input("삭제할 이름을 입력하시오: ")
        if name2 in friends :
            friends.remove(name2)
        else :
            print("없는이름임")
    elif menu == 4 :
        name3 = input("변경하고싶은 이름을 입력하시오: ")
        if name3 in friends :
            indx = friends.index(name3)
            name4 = input("새 이름을 입력하시오: ")
            friends[indx] = name4
        else :
            print("없는데?????")