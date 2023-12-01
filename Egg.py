import time
from PIL import ImageDraw, ImageFont

class Egg:
    def __init__(self, joystick, myImage, image_list, image_loader):
        self.joystick = joystick
        self.myImage = myImage
        self.image_list = image_list
        self.image_loader = image_loader
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
            # 남은 시간 계산
            remaining_time = 20 - int(time.time() - start_time)
            remaining_time = max(0, remaining_time)

            # 이미지 초기화
            self.myImage.paste(self.image_loader.get_image("eggBreak"), (0,0), self.image_loader.get_image("eggBreak"))
            self.myImage.paste(self.image_list[self.image_index], (60,50), self.image_list[self.image_index])
            #타이머 폰트 설정
            fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
            # 이미지에 남은 시간 표시
            my_draw = ImageDraw.Draw(self.myImage)
            my_draw.text((68, 9), str(remaining_time), font=fnt, fill=(0, 0, 0))
            # 이미지를 화면에 출력
            self.joystick.disp.image(self.myImage)

            if remaining_time <= 0: 
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
                if self.button_count >= 1:  # 여기 숫자 수정해야함 25로
                    return True
                time.sleep(0.2)

    def start(self):
        start_time = time.time()  # 시작 시간 저장
        return self.check_button(start_time)  # check_button 함수에 start_time을 인자로 전달합니다.
