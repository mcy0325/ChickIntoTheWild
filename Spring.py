import time
from PIL import Image
from Character import Character
from ImageLoader import ImageLoader
from Joystick import Joystick

class Spring:
    def __init__(self):
        self.joystick = Joystick() 
        self.image_loader = ImageLoader()
        self.character = Character()
        self.my_image = Image.new("RGB", (self.joystick.width, self.joystick.height))
        self.eggChick_image_list = [self.image_loader.get_image("eggChickMove1"), self.image_loader.get_image("eggChickMove2")]

    def start(self):
        while True:
            if self.joystick.button_L.value == False:  # L 버튼이 눌렸을 때
                self.character.switch_images(self.eggChick_image_list, mirror=True)
            elif self.joystick.button_R.value == False:  # R 버튼이 눌렸을 때
                self.character.switch_images(self.eggChick_image_list, mirror=False)
