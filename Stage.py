from Character import Character
from Enemy import Enemy
from Item import Item
from PIL import Image, ImageDraw, ImageFont
import time
import random

class Stage:
    def __init__(self, my_image, joystick, image_loader, lives, character_image1, character_image2, item_image_name, enemy_num, enemy_name, stage_duration, next_stage_image, next_stage_character, background_image_name, score_increment):
        self.my_image = my_image
        self.joystick = joystick
        self.image_loader = image_loader
        self.lives = lives #생명 수 
        self.character_images = (character_image1, character_image2) #캐릭터 이미지
        self.item_image_name = item_image_name #아이템 이미지 이름
        self.enemy_num = enemy_num #적의 수
        self.enemy_name = enemy_name #적의 이름
        self.stage_duration = stage_duration #스테이지 지속 시간
        self.next_stage_images = (next_stage_image, next_stage_character) #다음 스테이지로 넘어가는 이미지
        self.background_image_name = background_image_name #배경 이미지 이름
        self.score_increment = score_increment #점수 증가량
        #게임에 필요한 변수들 초기화
        self.my_image = None
        self.character = None
        self.items = None
        self.enemies = None
        self.lives_images = None
        self.start_time = None
        self.fnt = None
        self.score = 0

    #캐릭터, 아이템, 적 생성 함수
    def create_characters(self):
        self.character = Character(240, 240, self.image_loader.get_image(self.character_images[0]), self.image_loader.get_image(self.character_images[1]), self.my_image, self.joystick, self.image_loader)

    def create_items(self):
        item_image = self.image_loader.get_image(self.item_image_name)
        self.items = [Item(self.my_image, self.joystick.width, self.joystick.height, item_image) for _ in range(10)]
    
    def create_enemies(self):
        self.enemies = [Enemy(random.randint(20, 90), random.randint(20, 90), self.enemy_num, self.enemy_name, self.image_loader) for _ in range(self.enemy_num)]
    
    #화면에 표시하는 함수
    def draw_screen(self):
        self.my_image.paste(self.image_loader.get_image(self.background_image_name), (0,0), self.image_loader.get_image(self.background_image_name))
        for i, life_image in enumerate(self.lives_images):
            self.my_image.paste(life_image, (180 + i * 20, 10), life_image) 
        for item in self.items:
            item.display()
        for enemy in self.enemies:
            enemy.update()
            enemy.draw(self.my_image)
        remaining_time = self.stage_duration - int(time.time() - self.start_time)
        remaining_time = max(0, remaining_time)
        my_draw = ImageDraw.Draw(self.my_image)
        my_draw.text((68, 9), str(remaining_time), font=self.fnt, fill=(0, 0, 0))

    #게임 실행 함수
    def run(self):
        self.my_image = Image.new("RGB", (self.joystick.width, self.joystick.height))
        self.create_characters()
        self.create_items()
        self.create_enemies()
        self.lives_images = [self.image_loader.get_image("heart") for _ in range(self.lives)]
        self.start_time = time.time()
        self.fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        last_A_press_time = 0
        while True:
            self.character.move(self.joystick.get_commands())
            self.character.display()
            self.draw_screen()
            self.check_collision()
            #무적 기능 구현
            if self.joystick.button_A.value == False and self.character.special_count > 0:
                current_time = time.time()  
                if current_time - last_A_press_time > 0.2:  
                    self.character.special = True
                    self.character.special_start_time = current_time
                    self.character.special_count -= 1
                    last_A_press_time = current_time 
            if time.time() - self.start_time > self.stage_duration and len(self.items) <= 5:
                self.my_image.paste(self.image_loader.get_image(self.next_stage_images[0]), (0,0))
                self.my_image.paste(self.image_loader.get_image(self.next_stage_images[1]), (60,70), self.image_loader.get_image(self.next_stage_images[1]))
                self.joystick.disp.image(self.my_image)
                time.sleep(3)
                return True, self.score, self.lives
            #게임 오버 조건
            if self.lives == 0 or (time.time() - self.start_time > self.stage_duration and len(self.items) > 5):
                return False, self.score, self.lives       
    
    #충돌 체크 함수
    def collide(self, pos1, pos2, radius1, radius2):
        #두 객체의 위치와 반경을 이용해 충돌 여부 판단
        x1, y1 = pos1
        x2, y2 = pos2
        #두 위치 사이의 거리 계산
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 
        #두 반경의 합보다 거리가 작으면 충돌
        return distance < (radius1 + radius2 - 5) 

    #충돌 체크 및 제거 함수
    def check_collision(self):
        #충돌 여부 확인 후 충돌했다면 해당 객체 제거
        for item in self.items[:]:
            if self.collide(self.character.get_position(), item.get_position(), self.character.radius, item.radius):
                self.items.remove(item)
                if len(self.items) <= 5:
                    self.score += self.score_increment
        for enemy in reversed(self.enemies[:]):
            if self.character.special == False and self.collide(self.character.get_position(), enemy.get_position(), self.character.radius, enemy.radius):
                self.enemies.remove(enemy)
                self.lives -= 1
                if self.lives_images:
                    del self.lives_images[-1]
