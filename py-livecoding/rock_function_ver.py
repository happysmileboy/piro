import random

# def gamestart():
#
#
# gamestart() -> 실행 시
# print_intro() -> print해주기
# get_user_input() -> 실행 시 return input str
# calc_result() -> 실행하게 되면 return key -> value(win, draw, lost) +=1
# print_result() -> 실행 시 return print()

def gamestart():
    while True:
        print_intro()
        user = get_user_input()
        com = random.randint(1,3)
        result = calc_result(user, com)
        print_result(result)


def print_intro():
    intro_str = """가위 바위 보 게임!!!
    반가워요~~
    """
    print(intro_str)

def get_user_input():
    input_msg = '1. 가위, 2. 바위, 3. 보, (종료 :Q, q)'
    while True:
        input_str = input(input_msg)
        if input_str in ['1', '2', '3', 'q', 'Q']:
            if input_str in ['q', 'Q']:
                print("안녕히 가세요")
                exit()
            else:
                user = int(input_str)
                break
        else:
            print("잘못골랐습니다 다시 입력해주세요")
    return user

def calc_result(user, com):
    if user == com:
        result = "draw"
    elif user % 3 + 1 == com:
        result = "lost"
    elif com % 3 + 1 == user:
        result = "win"
    return result

def print_result(result):
    if result == "win":
        print("이겼습니다")
    elif result == "lost":
        print("졌습니다")
    else:
        print("비겼습니다")


gamestart()


#
# score_msg = "승 :{win}, 패 {lost}, 비김: {draw}"
#
# score = {'win': 0, 'draw': 0, 'lost': 0}
# rsp_set = ["가위", "바위", "보"]
#
# while True:
#     print(intro_str)
#                 print(score_msg.format(
#                     win=score['win'],
#                     draw=score['draw'],
#                     lost=score['lost']
#                 ))
#
#
#
#
# # # 1.가위바위보 메소드 -> if조건문
# # # 2.intro -> 반복문
# # # 3.승, 무, 패 저장 -> dict
# # # print input
#
# gamestart()
#
