# 🚀 Week 7: 파이썬 자료구조 II - 튜플, 딕셔너리, 세트, 문자열
# ㄴ(📖python express - 307p ~ 362p)

## 1. 튜플 (Tuple)
* **개념:** 리스트와 유사하지만, 한번 생성되면 **요소를 수정하거나 삭제할 수 없는(Immutable)** 변경 불가능합니다.
* **특징:** 소괄호 `()`를 사용하며, 실행 속도가 빠르고 데이터의 안전성이 보장됩니다.

## 2. 세트 (Set)
* 중괄호 {}를 사용하여 생성하고, 요소들의 순서가 없고, 중복된 값을 허용하지 않습니다.
* 
```Python
numbers = {1, 2, 3, 3, 2, 1}   # 세트 생성 예시
print(numbers)  # 출력: {1, 2, 3} (중복 제거)

numbers.add(4)     # 요소 추가
numbers.remove(1)  # 요소 삭제
```
### 📊 집합 연산
* **합집합:** set1 | set2 또는 set1.union(set2)
* **교집합:** set1 & set2 또는 set1.intersection(set2)
* **차집합:** set1 - set2 또는 set1.difference(set2)

## 3. 딕셔너리 (Dictionary)
* 키(Key)와 값(Value)의 쌍으로 데이터를 저장하는 자료구조입니다.
* 사전에서 단어를 찾듯 키를 통해 값을 매우 빠르게 검색할 수 있습니다. 키는 중복될 수 없지만, 값은 중복될 수 있습니다.

```Python
contacts = {"KIM": "123-4567", "PARK": "987-6543"}     # 딕셔너리 생성 예시

 # 데이터 참조 및 추가/수정
print(contacts["KIM"])       # 출력: 123-4567
contacts["LEE"] = "555-5555" # 새로운 쌍 추가

# 주요 메서드
print(contacts.keys())   # dict_keys(['KIM', 'PARK', 'LEE'])
print(contacts.values()) # dict_values(['123-4567', '987-6543', '555-5555'])
print(contacts.items())  # (Key, Value) 튜플 쌍 출력
```

## 4. 문자열 (String)
문자들이 연속되어 있는 시퀀스 자료형이며, 튜플과 마찬가지로 변경 불가능(Immutable)한 특징을 가집니다.

### 🔍 주요 문자열 메서드
#### 검색 및 대치:
* **`find(substring)`**: 문자열에서 특정 문자의 인덱스를 반환 (없으면 -1)
* **`replace(old, new)`**: 특정 문자를 다른 문자로 치환한 새로운 문자열 반환

### 분리 및 결합:
* **`split(separator)`**: 지정된 구분자를 기준으로 분리하여 리스트로 반환
* **`join(sequence)`**: 리스트의 요소들을 하나의 문자열로 결합

### 대소문자 변환 및 정제:
* **`upper()` / `lower()`**: 대문자 / 소문자 변환
* **`strip()`**: 양쪽 공백 제거

### 문자 종류 검사:
* **`isalpha()`**: 알파벳(한글 포함)으로만 구성되어 있는지 확인
* **`isdigit()`**: 숫자로만 구성되어 있는지 확인
* **`isspace()`**: 공백 문자로만 구성되어 있는지 확인
