from Character import Character
from Enemy import Enemy
from Item import Item
from PIL import ImageDraw, ImageFont
import time
import random

def stage_process(my_image, joystick, image_loader, lives, character_image1, character_image2, item_image_name, enemy_num, enemy_name, stage_duration, next_stage_image, next_stage_character, background_image_name, score_increment):
    # 캐릭터 생성
    character = Character(240, 240, image_loader.get_image(character_image1), image_loader.get_image(character_image2), my_image, joystick, image_loader)

    # 아이템 생성
    item_image = image_loader.get_image(item_image_name)
    items = [Item(my_image, joystick.width, joystick.height, item_image) for _ in range(10)]
    # 적 생성
    enemies = [Enemy(random.randint(20, 190), random.randint(20, 190), enemy_num, enemy_name, image_loader) for _ in range(enemy_num)]
    
    lives_images = [image_loader.get_image("heart") for _ in range(lives)]

    # 타이머 설정
    start_time = time.time()

    #타이머 폰트 설정
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    
    #점수
    score = 0

    # 게임 루프
    while True:
        # 캐릭터의 움직임 업데이트
        command = joystick.get_commands()
        character.move(command)
        character.display()

        #배경 이미지 출력
        my_image.paste(image_loader.get_image(background_image_name), (0,0), image_loader.get_image(background_image_name))

        # 생명 이미지 출력
        for i, life_image in enumerate(lives_images):
            my_image.paste(life_image, (180 + i * 20, 10), life_image) 

        # 아이템 출력
        for item in items:
            item.display()

        # 적의 움직임 업데이트 및 화면에 그리기
        for enemy in enemies:
            enemy.update()
            enemy.draw(my_image)

        # 남은 시간 출력
        remaining_time = stage_duration - int(time.time() - start_time)
        remaining_time = max(0, remaining_time)
        my_draw = ImageDraw.Draw(my_image)
        my_draw.text((68, 9), str(remaining_time), font=fnt, fill=(0, 0, 0))

        # 캐릭터와 아이템의 충돌 확인
        for item in items[:]:
            item_position = item.get_position()
            character_position = character.get_position()
            if collide(character_position, item_position):
                items.remove(item)
                print("아이템충돌")
                if len(items) <= 5:
                    score += score_increment
                    print(score)

        # 캐릭터와 적의 충돌 확인
        for enemy in enemies[:]:
            enemy_position = enemy.get_position()
            character_position = character.get_position()
            if collide(character_position, enemy_position):
                print("충돌")
                enemies.remove(enemy)
                lives -= 1
                # 생명 이미지 제거
                if lives_images:
                    del lives_images[-1]

        #루프 종료 조건1
        if time.time() - start_time > stage_duration and len(items) <= 5: #여기 시간 수정해야함
            my_image.paste(image_loader.get_image(next_stage_image), (0,0))
            my_image.paste(image_loader.get_image(next_stage_character), (60,70), image_loader.get_image(next_stage_character))
            joystick.disp.image(my_image)
            time.sleep(3)
            return True, score, lives
        
        # 루프 종료 조건2
        if lives == 0:
            return False, score, lives
        
        #루프 종료 조건3
        if time.time() - start_time > stage_duration and len(items) > 5:
            return False, score, lives

def collide(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5  # 두 위치 사이의 거리를 계산합니다.

    return distance < 16  # 거리가 10 이하면 충돌했다고 판단합니다.
