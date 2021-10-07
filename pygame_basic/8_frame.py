import pygame
###############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()   # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480   # 가로 크기
screen_height = 640   # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정 - 게임 화면이 뜰 때 글자로 표시
pygame.display.set_caption("게임 이름")   # 게임 이름

# FPS
clock = pygame.time.Clock()
###############################################################

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 폰트 등)


# 이동 속도
character_speed = 0.6

# 이벤트 루프
running = True   # 게임이 진행중인가?

while running:
    dt = clock.tick(60)   # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():   # 어떤 이벤트가 발생하였는가?(마우스나 키보드의 입력 및 동작이 들어오는지 확인)
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?(pygame 창을 껐을 때 발생)
            running = False   # 게임이 진행중이 아님(while문 탈출)

   
    # 3. 게임 캐릭터 위치 정의
    # for문을 나와 실제  캐릭터 x, y 좌표 바꿔주기
    # fps 값이 달라도 " 실제 게임 자체의 속도 "가 달라져서는 안 됨!! 
    # -> 이동의 부드러운 정도는 달라지되, 이동 속도가 달라지면 안 되므로 보정 거치기
    # 위치 좌표에 보정 처리
    # 가로 경계값 처리
    # 세로 경계값 처리
   
    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트

    # 5. 화면에 그리기

    # 매 프레임마다 화면을 새로 그려주는 동작
    pygame.display.update()   # 게임 화면을 다시 그리기! (계속해서 호출이 되어야 함.)


# pygame 종료
pygame.quit()
