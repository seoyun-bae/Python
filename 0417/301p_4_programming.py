list_old = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_new = [-i if 3 <= i <= 8 else i for i in list_old]

print(f"실행전 {list_old}")
print(f"실행후 {list_new}")