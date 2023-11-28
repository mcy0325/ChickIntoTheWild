import time
from Egg import Egg
from PIL import ImageDraw, ImageFont
from Stage import Stage

class Game:
    def __init__(self, joystick, image_loader):
        self.joystick = joystick
        self.image_loader = image_loader
        self.stage = 0
        self.scores = {
            'spring': 0,
            'summer': 0,
            'fall': 0,
            'winter': 0,
        }
        self.total_score = 0
        self.lives = 3   
        self.invincible = False
        self.invincible_time = 10
        self.invincible_uses = {
            'fall': 1,
            'winter': 1,
        }


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

    def run_stage(self, character_images, item_image, item_count, obstacle_image, obstacle_count, background_image, grown_image, stage_name, score_multiplier, invincible_images):
        game_stage = Stage(
            self.my_image, self.joystick, self.image_loader, self.lives,
            character_images[0], character_images[1], 
            item_image, item_count, 
            obstacle_image, obstacle_count, 
            background_image, grown_image, 
            stage_name, score_multiplier,
            invincible_images[0], invincible_images[1]
        )
        result, score, lives = game_stage.run()
        if not result:
            self.game_over_or_end("gameOver")
        return score, lives

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
            self.game_over_or_end("gameOver")
        else:
            self.my_image.paste(self.image_loader.get_image("growUp"), (0,0), self.image_loader.get_image("growUp"))
            self.my_image.paste(self.image_loader.get_image("eggChick"), (60,70), self.image_loader.get_image("eggChick"))
            self.joystick.disp.image(self.my_image)
            time.sleep(3)
            self.stage += 1

    def spring_stage(self):
        self.scores['spring'], self.lives = self.run_stage(["eggChickMove1", "eggChickMove2"], "bud", 4, "butterfly", 40, "growUp", "chick", "spring", 10, ["specialMove1", "specialMove2"])
        self.total_score += self.scores['spring']
        self.stage += 1

    def summer_stage(self):
        self.scores['summer'], self.lives = self.run_stage(["chickMove1", "chickMove2"], "waterDrop", 5, "cloud", 40, "growUp", "rooster", "summer", 20)
        self.total_score += self.scores['summer']
        self.stage += 1

    def fall_stage(self):
        self.scores['fall'], self.lives = self.run_stage(["roosterMove1", "roosterMove2"], "cherry", 6, "worm", 30, "growUp", "goodRooster", "fall", 30)
        self.total_score += self.scores['fall']
        self.stage += 1

    def winter_stage(self):
        self.scores['winter'], self.lives = self.run_stage(["goodRoosterMove1", "goodRoosterMove2"], "ice", 7, "sharp", 30, "growUp", "greatRooster", "winter", 40)
        self.total_score += self.scores['winter']
        self.my_image.paste(self.image_loader.get_image("totalScore"), (0,0), self.image_loader.get_image("totalScore"))
        fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        my_draw = ImageDraw.Draw(self.my_image)
        my_draw.text((105, 60), str(self.scores['spring']), font=fnt, fill=(0, 0, 0))
        my_draw.text((121, 95), str(self.scores['summer']), font=fnt, fill=(0, 0, 0))
        my_draw.text((80, 127), str(self.scores['fall']), font=fnt, fill=(0, 0, 0))
        my_draw.text((105, 162), str(self.scores['winter']), font=fnt, fill=(0, 0, 0))
        my_draw.text((98, 202), str(self.total_score), font=fnt, fill=(0, 0, 0))
        self.joystick.disp.image(self.my_image)
        time.sleep(5)
        self.game_over_or_end("gameEnd")

    def game_over_or_end(self, image_name):
        self.my_image.paste(self.image_loader.get_image(image_name), (0,0), self.image_loader.get_image(image_name))
        self.joystick.disp.image(self.my_image)

        while True:
            if self.joystick.button_B.value == False:
                self.reset_game()
                break

    def reset_game(self):
        self.stage = 0
        self.lives = 3
        self.scores = {
            'spring': 0,
            'summer': 0,
            'fall': 0,
            'winter': 0,
        }
        self.total_score = 0
        self.start(self.my_image)
