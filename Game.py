import time
import random
from Egg import Egg
from Character import Character
from Enemy import Enemy
from Item import Item

class Game:
    def __init__(self, joystick, image_loader, my_image):
        self.joystick = joystick
        self.image_loader = image_loader
        self.my_image = my_image
        self.stage = 0
        self.spring_score = 0
        self.lives = 3

    def start(self):
        while True:
            if self.stage == 0:
                self.start_stage()
            elif self.stage == 1:
                self.egg_break_stage()
            elif self.stage == 2:
                self.spring_stage()
            # elif self.stage == 3:
            #     self.summer_stage()
            # elif self.stage == 4:
            #     self.fall_stage()
            # elif self.stage == 5:
            #     self.winter_stage()
            else:
                break
    
    def game_over(self):
        self.my_image.paste(self.image_loader.get_image("gameOver"), (0,0), self.image_loader.get_image("gameOver"))
        self.joystick.disp.image(self.my_image)

        while True:
            if self.joystick.button_B.value == False:
                self.stage = 0
                self.start()
                break
    
    def start_stage(self):
        start_image_list = [self.image_loader.get_image("gameStart"), self.image_loader.get_image("gameStory1"), self.image_loader.get_image("gameStory2")]
        image_index = 0

        while image_index < len(start_image_list):
            self.my_image.paste(start_image_list[image_index], (0,0))
            self.joystick.disp.image(self.my_image)

            if self.joystick.button_A.value == False:
                image_index += 1
                time.sleep(0.2)

        self.stage += 1

    def egg_break_stage(self):
        self.my_image.paste(self.image_loader.get_image("eggBreak"), (0,0), self.image_loader.get_image("eggBreak"))
        self.my_image.paste(self.image_loader.get_image("egg1"), (60,50), self.image_loader.get_image("egg1"))
        self.joystick.disp.image(self.my_image)
        time.sleep(0.2)
        egg_image_list = [self.image_loader.get_image("egg2"), self.image_loader.get_image("egg3"), self.image_loader.get_image("egg4"), self.image_loader.get_image("egg5"), self.image_loader.get_image("egg6")]
        egg = Egg(self.joystick, self.my_image, egg_image_list)
        egg_success = egg.start()

        if not egg_success:
            self.game_over()
        
        else:
            self.my_image.paste(self.image_loader.get_image("growUp"), (0,0), self.image_loader.get_image("growUp"))
            self.my_image.paste(self.image_loader.get_image("eggChick"), (60,70), self.image_loader.get_image("eggChick"))
            self.joystick.disp.image(self.my_image)
            time.sleep(0.2)
            self.stage += 1


    def spring_stage(self):
        # 캐릭터 생성
        character = Character(240, 240, self.image_loader.get_image("eggChickMove1"), self.image_loader.get_image("eggChickMove2"), self.my_image, self.joystick, self.image_loader)
        # 아이템, 적의 위치 초기화
        item_positions = [[random.randint(20, 210), random.randint(20, 210)] for _ in range(10)]
        enemy_positions = [[random.randint(20, 210), random.randint(20, 210)] for _ in range(5)]

        # 아이템 생성
        item_image = self.image_loader.get_image("bud")
        items = [Item(self.my_image, self.joystick.width, self.joystick.height, item_image) for _ in range(10)]
        # 적 생성
        enemies = [Enemy(random.randint(20, 210), random.randint(20, 210), 5, "butterfly", self.image_loader) for _ in range(5)]
        # 타이머 설정
        start_time = time.time()
        
        
        # 게임 루프
        while True:
            if time.time() - start_time > 60:
                self.game_over()
                return
            

            # 캐릭터의 움직임 업데이트
            command = self.joystick.get_commands()  # 조이스틱의 입력을 받아옵니다. 이 부분은 조이스틱 라이브러리에 따라 다를 수 있습니다.
            character.move(command)
            character.display()

            self.my_image.paste(self.image_loader.get_image("spring"), (0,0), self.image_loader.get_image("spring")) 

            # 아이템과 적의 위치 업데이트
            item_positions, enemy_positions = self.update_positions(item_positions, enemy_positions)

            # 아이템 출력
            for item in items:
                item.display()

            # 적의 움직임 업데이트 및 화면에 그리기
            for enemy in enemies:
                enemy.update()
                enemy.draw(self.my_image)

            # 적 위치 출력
            for enemy in enemies:
                print("Enemy position:", enemy.get_position())

                                
            # 캐릭터와 아이템의 충돌 확인
            for item_position in item_positions:
                character_position = character.get_position()
                center_x = (character_position[0] + character_position[1]) / 2
                center_y = (character_position[0] + character_position[1]) / 2
                if self.collide([center_x, center_y], item_position):
                    item_positions.remove(item_position)
                    print("Item removed: ", item_position)
                    if len(item_positions) >= 4:
                        self.spring_score += 10

            # 캐릭터와 적의 충돌 확인
            for enemy in enemies:
                character_position = character.get_position()
                center_x = (character_position[0] + character_position[1]) / 2
                center_y = (character_position[0] + character_position[1]) / 2
                if self.collide([center_x, center_y], (enemy.x, enemy.y)):
                    self.lives -= 1
                    print("Enemy collided! Lives:", self.lives)

            # 생명이 0개가 되었는지 확인
            if self.lives == 0:
                self.game_over()  # 게임 오버 처리
                return  # 게임 루프 종료

            if time.time() - start_time > 60 and len(item_positions) <= 7:
                self.my_image.paste(self.image_loader.get_image("growUp"), (0,0))
                self.joystick.disp.image(self.my_image)
                self.stage += 1
                return
             
    
    def update_positions(self, item_positions, enemy_positions):
        # 아이템의 위치 업데이트
        for i in range(len(item_positions)):
            # 아이템이 화면 밖으로 나가지 않도록 제한
            item_positions[i][0] = max(0, min(item_positions[i][0], 200))
            item_positions[i][1] = max(0, min(item_positions[i][1], 200))

        # 적의 위치 업데이트
        for i in range(len(enemy_positions)):
            dx = random.randint(-5, 5)  # X 좌표를 -5부터 5까지 무작위로 이동
            dy = random.randint(-5, 5)  # Y 좌표를 -5부터 5까지 무작위로 이동

            # 이동 후의 위치가 화면을 벗어나는지 확인
            if 20 <= enemy_positions[i][0] + dx <= 210:
                enemy_positions[i][0] += dx
            if 20 <= enemy_positions[i][1] + dy <= 210:
                enemy_positions[i][1] += dy

        return item_positions, enemy_positions

    def collide(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2

        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5  # 두 위치 사이의 거리를 계산합니다.

        return distance < 10  # 거리가 10 이하면 충돌했다고 판단합니다.
