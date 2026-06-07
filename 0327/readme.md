# 🚀 Week 4: 반복문
# ㄴ(📖python express - 155p ~ 202p)

## 1. 횟수 제어 반복: `for` 문
### range() 함수 활용
* `range(stop)`: 0부터 `stop - 1`까지의 정수 시퀀스를 생성
* `range(start, stop)`: `start`부터 `stop - 1`까지의 정수 시퀀스를 생성
* `range(start, stop, step)`: `start`부터 `stop - 1`까지 `step`만큼씩 건너뛰는 정수 시퀀스를 생성

```python
# 0부터 4까지 총 5번 반복 실행
for i in range(5):
    print("현재 인덱스:", i)
```

## 2. 조건 제어 반복: while 문
* 특정 조건식이 참(True)인 동안 실행 블록을 계속해서 반복. 반복 횟수를 정확히 알 수 없을 때 주로 사용

```python
count = 1
while count <= 5:
    print("카운트:", count)
    count += 1  #필수
```

## 3. 루프 제어 명령어: break와 continue
* **break:** 특정 조건을 만족하면 반복문 전체를 즉시 탈출하고 다음 코드로 진행합니다. 주로 무한 루프와 조합하여 사용됩니다.
* **continue:** 아래에 있는 남은 코드를 건너뛰고, 반복문의 다음 차례(조건 검사 또는 다음 요소)로 즉시 이동합니다.
