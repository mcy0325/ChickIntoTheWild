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

    #이미지를 화면에 표시하는 함수
    def update_image(self):
        if self.image_index < len(self.image_list):
            self.myImage.paste(self.image_list[self.image_index], (60,50), self.image_list[self.image_index])
            self.joystick.disp.image(self.myImage)

    #버튼 누르는 것을 확인하는 함수
    def check_button(self, start_time):
        a_pressed = False #A버튼이 눌렸는지 여부
        while True:
            remaining_time = 15 - int(time.time() - start_time)
            remaining_time = max(0, remaining_time)

            self.myImage.paste(self.image_loader.get_image("eggBreak"), (0,0), self.image_loader.get_image("eggBreak"))
            self.myImage.paste(self.image_list[self.image_index], (60,50), self.image_list[self.image_index])

            fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
            #남은 시간 표시
            my_draw = ImageDraw.Draw(self.myImage)
            my_draw.text((68, 9), str(remaining_time), font=fnt, fill=(0, 0, 0))

            self.joystick.disp.image(self.myImage)

            if remaining_time <= 0: 
                return False
            if self.joystick.button_A.value == False:
                a_pressed = True #A버튼이 눌렸다는 상태 저장
                time.sleep(0.2)
            if self.joystick.button_B.value == False and a_pressed: # B 버튼이 눌렸고, 이전에 A 버튼이 눌렸으면
                self.button_count += 1 # 버튼 누른 횟수 증가
                a_pressed = False
                if self.button_count % 3 == 0: # 3번 눌렀을 때 이미지 업데이트
                    self.image_index += 1
                    self.update_image()
                if self.button_count >= 15: # 버튼을 15번 누르면 True 반환
                    return True
                time.sleep(0.2)
                
    #알 깨기 단계 시작 함수
    def start(self):
        start_time = time.time()  
        return self.check_button(start_time)  
