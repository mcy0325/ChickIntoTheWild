import time
from Egg import Egg
from PIL import ImageDraw, ImageFont
from Stage import stage_process

class Game:
    def __init__(self, joystick, image_loader):
        self.joystick = joystick
        self.image_loader = image_loader
        self.stage = 0
        self.spring_score = 0
        self.summer_score = 0
        self.fall_score = 0
        self.winter_score = 0
        self.total_score = 0
        self.lives = 3   

    def start(self, my_image):
        self.my_image = my_image
        while True:
            if self.stage == 0:
                self.start_stage()
            elif self.stage == 1:
                self.egg_break_stage()
            elif self.stage == 2:
                self.spring_stage()
            elif self.stage == 3:
                self.summer_stage()
            elif self.stage == 4:
                self.fall_stage()
            elif self.stage == 5:
                self.winter_stage()
            else:
                break
    
    def game_over(self):
        self.my_image.paste(self.image_loader.get_image("gameOver"), (0,0), self.image_loader.get_image("gameOver"))
        self.joystick.disp.image(self.my_image)

        while True:
            if self.joystick.button_B.value == False:
                self.stage = 0
                self.lives = 3
                self.spring_score = 0
                self.summer_score = 0
                self.fall_score = 0
                self.winter_score = 0
                self.total_score = 0
                self.start(self.my_image)
                break
    
    def game_end(self):
        self.my_image.paste(self.image_loader.get_image("gameEnd"), (0,0), self.image_loader.get_image("gameEnd"))
        self.joystick.disp.image(self.my_image)

        while True:
            if self.joystick.button_B.value == False:
                self.stage = 0
                self.lives = 3
                self.spring_score = 0
                self.summer_score = 0
                self.fall_score = 0
                self.winter_score = 0
                self.total_score = 0
                self.start(self.my_image)
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
        egg = Egg(self.joystick, self.my_image, egg_image_list, self.image_loader)
        egg_success = egg.start()

        if not egg_success:
            self.game_over()
        
        else:
            self.my_image.paste(self.image_loader.get_image("growUp"), (0,0), self.image_loader.get_image("growUp"))
            self.my_image.paste(self.image_loader.get_image("eggChick"), (60,70), self.image_loader.get_image("eggChick"))
            self.joystick.disp.image(self.my_image)
            time.sleep(3)
            self.stage += 1

    def spring_stage(self):
        result, score, lives = stage_process(self.my_image, self.joystick, self.image_loader, self.lives, "eggChickMove1", "eggChickMove2", "bud", 4, "butterfly", 40, "growUp", "chick", "spring", 10)
        if not result:
            self.game_over()
        else:
            self.spring_score = score
            self.total_score += self.spring_score
            self.lives = lives
            print(self.spring_score)
            print(self.total_score)
            self.stage += 1
    
    def summer_stage(self):
        result, score, lives = stage_process(self.my_image, self.joystick, self.image_loader, self.lives, "chickMove1", "chickMove2", "waterDrop", 6, "cloud", 40, "growUp", "rooster", "summer", 20)
        if not result:
            self.game_over()
        else:
            self.summer_score = score
            self.total_score += self.summer_score
            self.lives = lives
            print(self.summer_score)
            print(self.total_score)
            self.stage += 1

    def fall_stage(self):
        result, score, lives = stage_process(self.my_image, self.joystick, self.image_loader, self.lives, "roosterMove1", "roosterMove2", "cherry", 8, "worm", 30, "growUp", "goodRooster", "fall", 30)
        if not result:
            self.game_over()
        else:
            self.fall_score = score
            self.total_score += self.fall_score
            self.lives = lives
            print(self.fall_score)
            print(self.total_score)
            self.stage += 1

    def winter_stage(self):
        result, score, lives = stage_process(self.my_image, self.joystick, self.image_loader, self.lives, "goodRoosterMove1", "goodRoosterMove2", "ice", 10, "sharp", 30, "growUp", "greatRooster", "winter", 40)
        if not result:
            self.game_over()
        else:
            self.winter_score = score
            self.total_score += self.winter_score
            self.lives = lives
            print(self.winter_score)
            print(self.total_score)
            self.my_image.paste(self.image_loader.get_image("totalScore"), (0,0), self.image_loader.get_image("totalScore"))
            fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
            my_draw = ImageDraw.Draw(self.my_image)
            my_draw.text((105, 60), str(self.spring_score), font=fnt, fill=(0, 0, 0))
            my_draw.text((121, 95), str(self.summer_score), font=fnt, fill=(0, 0, 0))
            my_draw.text((80, 127), str(self.fall_score), font=fnt, fill=(0, 0, 0))
            my_draw.text((105, 162), str(self.winter_score), font=fnt, fill=(0, 0, 0))
            my_draw.text((98, 202), str(self.total_score), font=fnt, fill=(0, 0, 0))
            self.joystick.disp.image(self.my_image)
            time.sleep(5)
            self.game_end()