# Quiz) 하늘에서 떨어지는 돌 피하기 게임을 만드시오.

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동가능
# 2. 돌은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 돌을 피하면 다음 돌이 다시 떨어짐
# 4. 캐릭터가 돌과 충돌하면 게임 종료
# 5. FPS는 30으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480(세로 가로) - background.png
# 2. 캐릭터 : 70 * 70 - character.png
# 3. 돌 : 70 * 70 - enemy,png


import pygame
###############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()   # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480   # 가로 크기
screen_height = 640   # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정 - 게임 화면이 뜰 때 글자로 표시
pygame.display.set_caption("Quiz")   # 게임 이름

# FPS
clock = pygame.time.Clock()
###############################################################

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 폰트 등)
# 배경 만들기
background = pygame.image.load("/Users/simmigyeong/Documents/GitHub/vscode/pythonCourse/pygame_basic/background.png")

# 캐릭터 만들기
character = pygame.image.load("/Users/simmigyeong/Documents/GitHub/vscode/pythonCourse/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height - character_height)

# 이동 속도
character_spped = 0.6

# 이벤트 루프
running = True   # 게임이 진행중인가?

while running:
    dt = clock.tick(60)   # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():   # 어떤 이벤트가 발생하였는가?(마우스나 키보드의 입력 및 동작이 들어오는지 확인)
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?(pygame 창을 껐을 때 발생)
            running = False   # 게임이 진행중이 아님(while문 탈출)

   
    # 3. 게임 캐릭터 위치 정의
 
   
    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    # 매 프레임마다 화면을 새로 그려주는 동작
    pygame.display.update()   # 게임 화면을 다시 그리기! (계속해서 호출이 되어야 함.)


# pygame 종료
pygame.quit()
