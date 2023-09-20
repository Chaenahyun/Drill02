from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 초기 위치 설정
center_x, center_y = 400, 300
radius = 200
angle = 0

# 게임 루프
while True:
    clear_canvas()
    grass.draw(400, 30)

    # 원 모양의 경로를 따라 이동
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)

    character.draw(x, y)

    angle += math.radians(1)  # 1도씩 증가

    if angle >= math.radians(360):
        angle = 0  # 2π를 돌면 다시 처음으로

    update_canvas()
    delay(0.01)

close_canvas()
