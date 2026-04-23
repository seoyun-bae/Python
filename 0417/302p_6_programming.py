def check_common(list1, list2):
    for x in list1:
        if x in list2:
            return True
    return False

list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 7, 8, 9, 10]
print(check_common(list1, list2))