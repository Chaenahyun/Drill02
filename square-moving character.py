from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 초기 위치 설정
x, y = 0, 90
x_direction, y_direction = 1, 0  # 초기 이동 방향

# 좌표 리스트를 정의
path = [(100, 90), (100, 400), (700, 400), (700, 90)]

# 인덱스 설정
target_index = 0

# 게임 루프
while True:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)

    tx, ty = path[target_index]

    # 캐릭터 이동
    if x < tx:
        x += 2
    elif x > tx:
        x -= 2

    if y < ty:
        y += 2
    elif y > ty:
        y -= 2

    
    if x == tx and y == ty:
        target_index = (target_index + 1) % len(path)

    update_canvas()
    delay(0.01)

close_canvas()
