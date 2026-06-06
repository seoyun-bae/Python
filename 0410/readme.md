# 📂 Week 5: Python Functions (함수)

## 1. 함수의 개념 및 필요성
* **함수(Function):** 특정 작업을 수행하는 명령어들의 모음에 이름을 붙인 것입니다.
* **필요성:**
  * 소스 코드의 중복성을 없애줍니다.
  * 단순한 부분으로 분해할 수 있어 구조화된 프로그래밍이 가능합니다.
  * 한 번 작성된 함수는 다른 프로그램에서도 재사용할 수 있습니다.


## 2. 함수의 정의와 호출
파이썬에서는 `def` 키워드를 사용하여 함수를 정의하고, 함수의 이름을 써서 호출합니다.

```python
# 함수 정의 (Definition)
def get_area(radius):
    area = 3.14 * radius ** 2
    return area  # 결과 반환 및 함수 종료

# 함수 호출 (Call)
result = get_area(3)
```

## 3. 매개변수(Parameter)와 인수(Argument)
* **인수(Argument):** 함수를 호출할 때 함수에 전달하는 실제 값입니다. 
* **매개변수(Parameter):** 전달된 인수를 함수 내부에서 받아서 사용하는 변수입니다.

```python
value = get_sum(1, 10)  # 1과 10은 '인수'
def get_sum(start, end): # start와 end는 '매개변수'
    ...
```

## 4. 값 반환하기 (Return)
* 파이썬의 함수는 return을 사용하여 결과를 반환합니다. 
* 파이썬에서는 콤마(,)를 이용해 하나의 함수에서 여러 개의 값을 동시에 반환할 수 있습니다.

```python
def sub():
    return 1, 2, 3  # 3개의 값 반환

a, b, c = sub()     # 각각 변수에 풀어서 저장(Unpacking)
```

## 5. 변수의 범위 (Scope)
* **지역 변수 (Local Variable):** 함수 내부에서 정의된 변수로, 해당 함수 안에서만 접근할 수 있습니다. 함수가 호출될 때 생성되고 종료될 때 소멸합니다. 
* **전역 변수 (Global Variable):** 함수 외부에서 정의된 변수로, 프로그램 전체에서 읽을 수 있습니다. 
* **global 키워드:** 함수 내부에서 전역 변수의 값을 변경하고자 할 때 사용합니다.

```python
gx = 100  # 전역 변수

def myfunc():
    global gx  # 전역 변수 gx를 사용하겠다고 명시
    gx = 200   # 전역 변수 값 변경

myfunc()
print(gx)  # 출력: 200
```

## 6. 순환 호출(Recursion)
* **순환(재귀):** 함수가 자기 자신을 다시 호출하여 문제를 해결하는 프로그래밍 기법입니다. 
* **대표 예시 (팩토리얼 계산):**
```python
  def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # 자기 자신 호출
```
