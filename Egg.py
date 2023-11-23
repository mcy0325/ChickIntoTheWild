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
        # 이미지 인덱스가 이미지 리스트의 길이를 넘지 않을 때만 이미지를 업데이트합니다.
        if self.image_index < len(self.image_list):
            self.myImage.paste(self.image_list[self.image_index], (60,50), self.image_list[self.image_index])
            self.joystick.disp.image(self.myImage)
        else:
            print("All images have been displayed.")


    def check_button(self):
        a_pressed = False
        while True:
            if self.joystick.button_A.value == False:
                a_pressed = True
                time.sleep(0.2)
            if self.joystick.button_B.value == False and a_pressed:
                self.button_count += 1
                a_pressed = False
                if self.button_count % 5 == 0:
                    self.image_index += 1
                    self.update_image()
                if self.button_count >= 25:  # button_count가 25 이상이면 True를 반환
                    return True
                time.sleep(0.2)
        return False

    def start(self):
        start_time = time.time()  # 시작 시간 저장
        while True:
            if time.time() - start_time > 10:  # 10초를 초과하면 종료
                print("시간 초과!")
                return False
            if self.check_button():  # 버튼 확인, check_button이 True를 반환하면 True 반환
                return True

