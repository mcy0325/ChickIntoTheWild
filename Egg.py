import time
from PIL import Image
from colorsys import hsv_to_rgb

class Egg:
    def __init__(self, joystick, myImage, image_list):
        self.joystick = joystick
        self.myImage = myImage
        self.image_list = image_list
        self.image_index = 0
        self.button_count = 0

    def update_image(self):
        self.myImage.paste(self.image_list[self.image_index], (0,0), mask=self.image_list[self.image_index])
        self.joystick.disp.image(self.myImage)

    def check_button(self):
        if self.joystick.button_A.value == False or self.joystick.button_B.value == False:
            self.button_count += 1
            # 5번마다 이미지를 변경합니다.
            if self.button_count % 5 == 0:
                self.image_index += 1
                self.update_image()
            # 30번 버튼이 눌렸을 때, while 문을 종료합니다.
            if self.button_count == 30:
                return False
            time.sleep(0.2)
        return True

    def start(self):
        while True:
            if not self.check_button():
                break