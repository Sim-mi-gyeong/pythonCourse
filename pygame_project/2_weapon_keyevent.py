import pygame
import os
###############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()   # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 640   # 가로 크기
screen_height = 480   # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정 - 게임 화면이 뜰 때 글자로 표시
pygame.display.set_caption("Nado Pang")   # 게임 이름

# FPS
clock = pygame.time.Clock()
###############################################################

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 폰트 등)
current_path = os.path.dirname(__file__)   # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")   # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))
 
# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size   
stage_height = stage_size[1]   # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height) - (character_height) - (stage_height)

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]   # width만 필요한 이유: 캐릭터가 무기를 쏠 때 중앙에서 나옴 -> 중앙 처리 : 캐릭터 width/2 - 무기 width/2 한 위치 

# 무기는 한 번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 이벤트 루프
running = True   # 게임이 진행중인가?

while running:
    dt = clock.tick(60)   # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():   # 어떤 이벤트가 발생하였는가?(마우스나 키보드의 입력 및 동작이 들어오는지 확인)
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?(pygame 창을 껐을 때 발생)
            running = False   # 게임이 진행중이 아님(while문 탈출)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:   # 캐릭터를 왼쪽으로
                character_to_x -= character_speed

            elif event.key == pygame.K_RIGHT:   # 캐릭터를 오른쪽으로
                character_to_x += character_speed

            elif event.key == pygame.K_SPACE:   # 무기 발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)   # 무기를 발사한 위치 정의 - 플레이어의 위치 중앙
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])   # 무기를 여러 번 쏠 경우 (x,y) 값이 여러 개가 나올 것

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
   
    # 무기 위치 조정
    # 100, 200 -> 180, 160, 140, ...
    # 500, 200 -> 180, 160, 140, ...
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]   # 무기 위치를 위로 올림

    # 천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]   # 천장에 닿지 않은 것에 대해서만 리스트로 . 

    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트

    # 5. 화면에 그리기
    screen.blit(background, (0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    # 무기 위치에 해당하는 부분을 가장 아래 하면, 배경이 그려지고 -> 그 위에 stage가 그려지고 -> 캐릭터가 그려지고 -> 무기가 그려져
    # 캐릭터 위를 무기가 지나가게됨. -> stage 위로 코드 위치 변경
    # for weapon_x_pos, weapon_y_pos in weapons:
    #     screen.blit(weapon, (weapon_x_pos, weapon_y_pos))


    # 매 프레임마다 화면을 새로 그려주는 동작
    pygame.display.update()   # 게임 화면을 다시 그리기! (계속해서 호출이 되어야 함.)


# pygame 종료
pygame.quit()
