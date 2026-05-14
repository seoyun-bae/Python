score_dic = {}

while True:
    name = input("학생 이름을 입력하세요 (종료하려면 'q' 입력): ")
    
    if name.lower() == 'q':
        break
        
    scores_input = input(f"{name} 학생의 성적(국어 영어 수학)을 입력하세요: ")
    
    score_list = list(map(int, scores_input.split()))
    
    score_dic[name] = score_list

print("\n--- 성적 처리 결과 ---")

for name, scores in score_dic.items():
    average = sum(scores) / len(scores)
    print(f"{name}의 평균성적 = {average}")