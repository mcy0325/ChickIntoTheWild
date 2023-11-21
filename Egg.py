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
        self.myImage.paste(self.image_list[self.image_index], (60,50), self.image_list[self.image_index])
        self.joystick.disp.image(self.myImage)

    def check_button(self):
        if self.joystick.button_A.value == False or self.joystick.button_B.value == False:
            self.button_count += 1
            # 5번마다 이미지를 변경합니다.
            if self.button_count % 5 == 0:
                self.image_index += 1
                self.update_image()
            # 30번 버튼이 눌렸을 때, while 문을 종료합니다.
            if self.button_count == 25:
                return False
            time.sleep(0.2)
        return True

    def start(self):
        start_time = time.time()  # 시작 시간 저장
        while True:
            if self.button_count >= 25:
                return True
            if not self.check_button():  # 버튼 확인
                return False
            if time.time() - start_time > 10:  # 10초를 초과하면 종료
                print("시간 초과!")
                return False
        
