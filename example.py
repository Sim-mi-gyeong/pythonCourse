# #Skeleton Code

# import string
# import random

# class Player:
#     def __init__(self, name, hp, damage, correct_alp):
#         self.name = name      # 이름
#         self.hp = hp          # 생명력
#         self.damage = damage  # 데미지
#         self.correct_alp = 0  # 알파벳 맞춘 횟수


# class Game:

#     def __init__(self):
#         self.player = []  # 캐릭터의 목록. start_game()에서 생성
#         self.user_character = ""  # 사용자가 선택한 캐릭터
#         self.remain_alp = list(string.ascii_uppercase)  # 남은 알파벳
#         self.cur_string = ["_"] * 10  # 현재까지의 글자상태를 저장
#         self.answer_string = ""  # 랜덤 10글자 단어

#     def start_game(self):
        
#         # - [ 게임 시작 전 ] 부분을 담당하는 함수 입니다.
#         # - 캐릭터들을 초기화 하고, 사용자가 플레이할 캐릭터를 선택합니다.
#         # - 랜덤 알파벳 10글자로 이루어진 answer_string 을 생성합니다.
#         # - 동일 클래스의 game()에서 호출됩니다.

# 		self.player.append(Player("김건웅", 50, 20, 0))
#         self.player.append(Player("김현주", 70, 25, 0))
#         self.player.append(Player("박진혁", 80, 30, 0))
#         self.player.append(Player("유송경", 90, 35, 0))

#         # (1): 사용자의 캐릭터 선택하여 user_character에 저장해주세요.
#         for i in Player:
#             user_character = i

#         # (2) : 랜덤 알파벳 10글자로 이루어진 단어 만들어 answer_string에 저장해주세요.
#         num = 10
#         for i in range(num):
#             answer_string = ''.join(random.choice(string.ascii_uppercases))

#     def sort_data(self, i):        
		
#         # - [ 게임 진행 ] 부분에서 게임진행 순서를 담당하는 함수 입니다.
#         # - 동일 클래스의 game()에서 호출됩니다.
       
#         # TODO : ROUND 1 일 땐 이름순/ ROUDN 2,3 일 땐 HP 순 게임진행을 위한 data 를 재정렬해주세요.
#         # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.

#         return player
#     def play_game(self):
#         """ 
#         - [ 게임 진행 ] 부분을 담당하는 함수 입니다.
#         - 동일 클래스의 game()에서 호출됩니다.
#         """

#         print(
#             f"게임은 {self.player[0].name},{self.player[1].name},{self.player[2].name},{self.player[3].name} 순으로 진행됩니다.\n")

#         for i in range(4):

#             if self.player[i] == self.user_character:
#                 print("***** 내 캐릭터 *****")
#             else:
#                 print(f"***** {i+1} 캐릭터 *****")

#             print(f"이름: {self.player[i].name} (HP: {self.player[i].hp})")

#             # TODO (1) : 랜덤의 알파벳 한글자를 선택하게 해주세요. 
# 						# 단 앞에 나왔던 알파벳과 중복되면 안됩니다.

#             # TODO (2) : 선택된 알파벳이 맞았을 시에, 현재까지 맞춘 단어의 상태를 출력해주세요.
#             #  print("***** 맞았습니다 ᵔεᵔ  *****")

#             # TODO (3) : 선택된 알파벳이 틀렸을 시에, 생명력을 데미지 만큼 감소시켜주고 이를 출력해주세요.
#             #  print("***** 틀렸습니다 (ﾟ⊿ﾟ)  ******")

#     def game_result(self):
#         """
#         - [ 게임 종료 후 ] 부분을 담당하는 함수 입니다.
#         - 게임의 결과를 생명력순, 알파벳 맞춘 횟수 순 두가지의 경우로 출력해야 합니다.
#         - 동일 클래스의 game()에서 호출됩니다.
#         """

#         print("\n\n******************* 게임이 끝났습니다 *******************")

#         # TODO (1) : 생명력 순으로 결과값을 출력해주세요.
#         # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
#         print("=============================")
#         print("     게임 순위 - 생명력")
#         print("=============================")

#         # TODO (2) : 알파벳 맞춘 횟수 순으로 결과값을 출력해주세요.
#         # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
#         print("=============================")
#         print(" 게임 순위 - 알파벳 맞춘 횟수")
#         print("=============================")

#     def game(self):
        
#         # - 게임 운영을 위한 함수입니다. 
#         # - 별도의 코드 작성이 필요 없습니다. 
    

#         self.start_game()

#         print("******************* 게임 시작 *******************\n")

#         for i in range(1, 4):
#             print("===========================")
#             print(f"     ROUND {i} - START")
#             print("===========================")

#             self.sort_data(i)
#             self.play_game()

#             print("===========================")
#             print(f"     ROUND {i} - END")
#             print("===========================")

#         self.game_result()

# if __name__ == '__main__':

#     """
#     - 코드를 실행하는 부분입니다. 
#     - 역시 별도의 코드 작성이 필요 없습니다. 
#     """
#     game = Game()
#     game.game()
