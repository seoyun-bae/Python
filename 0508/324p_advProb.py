s1 = input("첫 번째 문자열: ")
s2 = input("두 번째 문자열: ")

set1 = set(s1)
set2 = set(s2)
common_chars = set1 & set2

list1 = list(common_chars)

print("\n공통적인 글자:", end=" ")
for i in list1:
    print(i, end=" ")
print() 


total_unique_chars = len(set1 | set2)


if total_unique_chars > 0:
    ratio = len(common_chars) / total_unique_chars
    
    if ratio >= 0.7:
        print(f"공통 비율: {ratio*100:.1f}%")
        print("표절 의심")
    else:
        print(f"공통 비율: {ratio*100:.1f}% - 정상입니다.")