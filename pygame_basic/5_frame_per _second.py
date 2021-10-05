import pygame

pygame.init()   # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480   # 가로 크기
screen_height = 640   # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정 - 게임 화면이 뜰 때 글자로 표시
pygame.display.set_caption("Nado Game")   # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("/Users/simmigyeong/Documents/GitHub/vscode/pythonCourse/pygame_basic/background.png")

# 배경 이미지가 왼쪽 위 (0,0)을 기준으로 크기가 설정되듯이, 캐릭터 역시 캐릭터 크기에서 왼쪽 위 지점을 알아야 함. -> 계산
# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/simmigyeong/Documents/GitHub/vscode/pythonCourse/pygame_basic/character.png")
character_size = character.get_rect().size   # 이미지의 크기를 구해옴. (70, 70)
character_width = character_size[0]   # 캐릭터의 가로 크기
character_height = character_size[1]   # 캐릭터의 세로 크기
character_x_pos =  (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로 위치)(x, y 좌표 기준 상하좌우로 움직일 수 있음)
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 해당하는 곳에 위치(세로 위치)

# 이동할 좌쵸
to_x = 0
to_y = 0

# 이벤트 루프
running = True   # 게임이 진행중인가?

while running:
    dt = clock.tick(60)   # 게임화면의 초당 프레임 수를 설정

    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():   # 어떤 이벤트가 발생하였는가?(마우스나 키보드의 입력 및 동작이 들어오는지 확인)
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?(pygame 창을 껐을 때 발생)
            running = False   # 게임이 진행중이 아님(while문 탈출)

        if event.type == pygame.KEYDOWN:   # 키가 눌렸는지 확인
            if event.key == pygame.K_LEFT:   # 캐릭터를 왼쪽으로
                to_x -= 5
            elif event.key == pygame.K_RIGHT:   # 캐릭터를 오른쪽으로
                to_x += 5
            elif event.key == pygame.K_UP:   # 캐릭터를 위쪽으로 
                to_y -= 5
            elif event.key == pygame.K_DOWN:   # 캐릭터를 아래쪽으로 
                to_y += 5

        if event.type == pygame.KEYUP:   # 방향키를 떼면 멈춤
            # x 좌표 기준 왼쪽이나 오른쪽으로 방향키를 누르고 있다가 떼면 0으로 설정
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0   # 움직이지 X
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # for문을 나와 실제  캐릭터 x, y 좌표 바꿔주기
    character_x_pos += to_x
    character_y_pos += to_y 

    # 가로 경계값 처리
    if character_x_pos < 0:   # 화면 왼쪽으로 벗어나면
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:   # 화면 오른쪽으로 벗어나면 
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:   # 화면 위로 벗어나면
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:   # 화면 아래로 벗어나면 
        character_y_pos = screen_height - character_height


    # background 이미지를 실제로 그려줌.
    screen.blit(background, (0, 0))   # 배경 그리기 / (0,0)은 가장 왼쪽 위
    
    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))


    # 매 프레임마다 화면을 새로 그려주는 동작
    pygame.display.update()   # 게임 화면을 다시 그리기! (계속해서 호출이 되어야 함.)


# pygame 종료
pygame.quit()
