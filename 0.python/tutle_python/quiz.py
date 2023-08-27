# 파이썬으로 퀴즈 만들기
# 퀴즈 문제와 정답을 저장하는 딕셔너리
quiz_dict = {
    "사과를 영어로 하면?": "apple",
    "책을 영어로 하면?": "book",
    "꽃을 영어로 하면?": "flower",
    "물을 영어로 하면?": "water",
    "책상을 영어로 하면?": "desk",
}

# 점수를 저장할 변수
score = 0

# 퀴즈 문제를 순서대로 출력하고 사용자의 답을 입력받는 반복문
for question, answer in quiz_dict.items():
    print(question)
    user_answer = input("답: ")
    # 사용자의 답과 정답을 비교하고 점수를 증가시키는 조건문
    if user_answer == answer:
        print("정답입니다!")
        score += 1
    else:
        print("틀렸습니다.")
        print(f"정답은 {answer}입니다.")

# 최종 점수를 출력하는 문장
print(f"총 {len(quiz_dict)}문제 중 {score}문제를 맞추셨습니다.")

