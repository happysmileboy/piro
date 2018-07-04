import random

intro_str = """가위 바위 보 게임!!!
반가워요~~
"""
input_msg = '1. 가위, 2. 바위, 3. 보, (종료 :Q, q)'
score_msg = "승 :{win}, 패 {lost}, 비김: {draw}"

score = {'win' : 0, 'draw': 0, 'lost':0}
rsp_set = ["가위", "바위", "보"]


while True:
    print(intro_str)
    while True:
        input_str = input(input_msg)
        if input_str in ['1','2','3','q','Q']:
            if input_str in['q','Q']:
                print("안녕히 가세요")
                exit()
            else:
                user = int(input_str)
                com = random.randint(1, 3)

                if user == com:
                    print("비겼습니다.")
                    score['draw'] += 1
                elif user % 3 + 1 == com:
                    print("졌습니다")
                    score['lost'] += 1
                elif com % 3 + 1 == user:x
                    print("이겼습니다.")
                    score['win'] +=1

                print(score_msg.format(
                    win = score['win'],
                    draw = score['draw'],
                    lost = score['lost']
                ))
        else:
            print("잘못골랐습니다 다시 입력해주세요")


#
#
#
# input_str = input("무엇을 내시겠습니까?")
# #input_str =="q, Q" -> 게임을 종료
#
#
#
# 9가지 가위 1, 2, 3
# com_str = random.randint(1,3)
#
# 가위 = 1
# 바위 = 2
# 보 = 3
#
# user_str == com_str -> 비김 : score[drow] 1을 상승시킨다
# 가 < 바위 가위 +1 == 바위
# 바위 <보 바위 +1 == 보
# 보< 가위 보 +1=4 % 3 ==가위 = 1
#
# if user == com:
#     user의 draw 1상승
# elif user % 3 + 1 == com:
#     user의 lost 1상승합니다
# elif com % 3 + 1 == user:
#     user의 win 1 상승하게
#     if 됩니다:
#
#
#
#
# (user + 1) % 3
#
#
#
# # 1.가위바위보 메소드 -> if조건문
# # 2.intro -> 반복문
# # 3.승, 무, 패 저장 -> dict
# # print input
