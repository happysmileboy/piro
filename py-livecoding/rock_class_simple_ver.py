import random


# # # 1.가위바위보 메소드 -> if조건문
# # # 2.intro -> 반복문
# # # 3.승, 무, 패 저장 -> dict
# # # print input
#

class game():
    intro_msg = "가위 바위 보 게임 !! 안녕하세요"
    input_msg = "1. 가위 2. 바위 3. 보, 종료(q, Q)"
    choice_list = ('가위', '바위', '보')
    print_confirm_msg = "{user}를 내셨군요. 저는 {com}냈습니다."
    user = None
    com = None
    result = None

    def start(self):
        while True:
            self.intro()  # -> 인트로메세지를출력합니다
            self.user = self.get_user_input()  # ->
            self.com = random.randint(1, 3)  # -> 가위바위보생성
            self.calc_result()  # -> 결과값도출(win, draw, lost)
            self.print_result()  # -> print


    def intro(self):
        print(self.intro_msg)


    def get_user_input(self):
        while True:
            input_str = input(self.input_msg)
            if input_str in ['1', '2', '3', 'q', 'Q']:
                if input_str in ['q', 'Q']:
                    print("안녕히 가세요")
                    exit()
                else:
                    return int(input_str)
                    break
            else:
                print("잘못골랐습니다 다시 입력해주세요")
        return user


    def calc_result(self):
        if self.user == self.com:
            self.result = "draw"
        elif self.user % 3 + 1 == self.com:
            self.result = "lost"
        elif self.com % 3 + 1 == self.user:
            self.result = "win"


    def print_result(self):
        if self.result == "win":
            print("이겼습니다")
        elif self.result == "lost":
            print("졌습니다")
        else:
            print("비겼습니다")

rock = game()
rock.start()


#
# class -> 데이터를 만드는 form, 틀
# instance class로 만들어진 과자 data 뭉치 덩어리
#
# userinterface - # print_intro() -> print해주기 + # print_result() -> 실행 시 return print()
# game - # get_user_input() -> 실행 시 return input str
# # calc_result() -> 실행하게 되면 return key -> value(win, draw, lost) +=1
# # score manager() 제가 올려드릴게용
#
# class game():
#     intro_msg = '1. 가위, 2. 바위, 3. 보, (종료 :Q, q)'
#
#
#     def calc_result(user, com):
#         if user == com:
#             result = "draw"
#         elif user % 3 + 1 == com:
#             result = "lost"
#         elif com % 3 + 1 == user:
#             result = "win"
#         return result
#
#
#         print_intro()
#         user = get_user_input()
#         com = random.randint(1,3)
#         result = calc_result(user, com)
#         print_result(result)
#
#
# rock = game()
# rock.start()
#
#
#
# rock = game()
#
# # gamestart() -> 실행 시
# # print_intro() -> print해주기
# # get_user_input() -> 실행 시 return input str
# # calc_result() -> 실행하게 되면 return key -> value(win, draw, lost) +=1
# print_result() -> 실행 시 return print()
