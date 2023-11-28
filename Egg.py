import time

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

    def check_button(self, start_time):
        a_pressed = False
        while True:
            if time.time() - start_time > 20:  # 여기 숫자 수정해야함 15로
                return False
            if self.joystick.button_A.value == False:
                a_pressed = True
                time.sleep(0.2)
            if self.joystick.button_B.value == False and a_pressed:
                self.button_count += 1
                a_pressed = False
                if self.button_count % 5 == 0:
                    self.image_index += 1
                    self.update_image()
                if self.button_count >= 25:  # 여기 숫자 수정해야함 25로
                    return True
                time.sleep(0.2)

    def start(self):
        start_time = time.time()  # 시작 시간 저장
        return self.check_button(start_time)  # check_button 함수에 start_time을 인자로 전달합니다.


