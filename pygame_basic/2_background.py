import pygame

pygame.init()   # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480   # 가로 크기
screen_height = 640   # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정 - 게임 화면이 뜰 때 글자로 표시
pygame.display.set_caption("Nado Game")   # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("/Users/simmigyeong/Documents/GitHub/vscode/pythonCourse/pygame_basic/background.png")


# 이벤트 루프
running = True   # 게임이 진행중인가?

while running:
    for event in pygame.event.get():   # 어떤 이벤트가 발생하였는가?(마우스나 키보드의 입력 및 동작이 들어오는지 확인)
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?(pygame 창을 껐을 때 발생)
            running = False   # 게임이 진행중이 아님(while문 탈출)

    # screen.fill((0, 0, 255))   # (R, G, B) 값
    # background 이미지를 실제로 그려줌.
    screen.blit(background, (0, 0))   # 배경 그리기 / (0,0)은 가장 왼쪽 위

    # 매 프레임마다 화면을 새로 그려주는 동작
    pygame.display.update()   # 게임 화면을 다시 그리기! (계속해서 호출이 되어야 함.)


# pygame 종료
pygame.quit()
