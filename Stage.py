from Character import Character
from Enemy import Enemy
from Item import Item
from PIL import Image, ImageDraw, ImageFont
import time
import random

class Stage:
    def __init__(self, my_image, joystick, image_loader, lives, character_image1, character_image2, item_image_name, enemy_num, enemy_name, stage_duration, next_stage_image, next_stage_character, background_image_name, score_increment, invincible_image1, invincible_image2):
        self.my_image = my_image
        self.joystick = joystick
        self.image_loader = image_loader
        self.lives = lives
        self.character_images = (character_image1, character_image2)
        self.item_image_name = item_image_name
        self.enemy_num = enemy_num
        self.enemy_name = enemy_name
        self.stage_duration = stage_duration
        self.next_stage_images = (next_stage_image, next_stage_character)
        self.background_image_name = background_image_name
        self.score_increment = score_increment
        self.invincible_images = (invincible_image1, invincible_image2)
        self.invincible = False
        self.my_image = None
        self.character = None
        self.items = None
        self.enemies = None
        self.lives_images = None
        self.start_time = None
        self.fnt = None
        self.score = 0

    def create_characters(self):
        self.character = Character(240, 240, self.image_loader.get_image(self.character_images[0]), self.image_loader.get_image(self.character_images[1]), self.my_image, self.joystick, self.image_loader, self.image_loader.get_image(self.invincible_images[0], self.image_loader.get_image(self.invincible_images[1])))

    def create_items(self):
        item_image = self.image_loader.get_image(self.item_image_name)
        self.items = [Item(self.my_image, self.joystick.width, self.joystick.height, item_image) for _ in range(10)]
    
    def create_enemies(self):
        self.enemies = [Enemy(random.randint(20, 190), random.randint(20, 190), self.enemy_num, self.enemy_name, self.image_loader) for _ in range(self.enemy_num)]
    
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

    def run(self):
        self.my_image = Image.new("RGB", (self.joystick.width, self.joystick.height))
        self.create_characters()
        self.create_items()
        self.create_enemies()
        self.lives_images = [self.image_loader.get_image("heart") for _ in range(self.lives)]
        self.start_time = time.time()
        self.fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        while True:
            self.character.move(self.joystick.get_commands(), self.invincible)
            self.character.display()
            self.draw_screen()
            self.check_collision()
            if self.joystick.button_A.value == False:
                self.invincible = True
                time.sleep(5)
                self.invincible = False
            if time.time() - self.start_time > self.stage_duration and len(self.items) <= 5:
                self.my_image.paste(self.image_loader.get_image(self.next_stage_images[0]), (0,0))
                self.my_image.paste(self.image_loader.get_image(self.next_stage_images[1]), (60,70), self.image_loader.get_image(self.next_stage_images[1]))
                self.joystick.disp.image(self.my_image)
                time.sleep(3)
                return True, self.score, self.lives
            if self.lives == 0 or (time.time() - self.start_time > self.stage_duration and len(self.items) > 5):
                return False, self.score, self.lives       

    def collide(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2

        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5  # 두 위치 사이의 거리를 계산합니다.

        return distance < 16  # 거리가 10 이하면 충돌했다고 판단합니다.

    def check_collision(self):
        for item in self.items[:]:
            if self.collide(self.character.get_position(), item.get_position()):
                self.items.remove(item)
                if len(self.items) <= 5:
                    self.score += self.score_increment
        for enemy in self.enemies[:]:
            if self.collide(self.character.get_position(), enemy.get_position()):
                self.enemies.remove(enemy)
                if not self.invincible:
                    self.lives -= 1
                    if self.lives_images:
                        del self.lives_images[-1]
