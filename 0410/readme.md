# 🚀 Week 5: Python Functions (함수)
# ㄴ(📖python express - 203p ~ 250p)

## 1. 함수의 개념 및 필요성
* **함수(`def`):** 특정 작업을 수행하는 명령어들의 모음에 이름을 붙인 것입니다.
* **필요성:**
  * 소스 코드의 중복성을 없애줍니다.
  * 단순한 부분으로 분해할 수 있어 구조화된 프로그래밍이 가능합니다.
  * 한 번 작성된 함수는 다른 프로그램에서도 재사용할 수 있습니다.

```python
def get_area(radius):
    area = 3.14 * radius ** 2
    return area  # 결과 반환 및 함수 종료

result = get_area(3)   # 함수 호출
```

## 2. 인수(Argument)와 매개변수(Parameter)
* **인수(Argument):** 함수를 호출할 때 함수에 전달하는 실제 값입니다. 
* **매개변수(Parameter):** 전달된 인수를 함수 내부에서 받아서 사용하는 변수입니다.

```python
value = get_sum(1, 10)  # 1과 10은 '인수'
def get_sum(start, end): # start와 end는 '매개변수'
    ...
```

## 3. 변수의 범위 (Scope)
* **지역 변수 (Local Variable):** 함수 내부에서 정의된 변수로, 해당 함수 안에서만 접근할 수 있습니다.
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

## 4. 순환 호출
* **순환(재귀):** 함수가 자기 자신을 다시 호출하여 문제를 해결하는 프로그래밍 기법입니다. 
