from PIL import ImageOps
from ImageLoader import ImageLoader
import time
from Joystick import Joystick

def mirror_image(image):
    return ImageOps.mirror(image)

def switch_images(self, images, mirror=False):
    x_coordinate = 60  # 초기 x 좌표
    while True:
        if self.joystick.button_L.value == False and mirror:  # L 버튼이 눌리고 mirror가 True일 때
            mirrored_image = mirror_image(images[self.image_index])
            self.myImage.paste(mirrored_image, (x_coordinate, 50), mirrored_image)
            self.joystick.disp.image(self.myImage)
            self.image_index = (self.image_index + 1) % len(images)  # 다음 이미지로 인덱스를 변경
            x_coordinate -= 10  # 이미지를 왼쪽으로 이동
            time.sleep(0.1)  # 이미지 전환 속도를 조절하는 데 사용

        elif self.joystick.button_R.value == False and not mirror:  # R 버튼이 눌리고 mirror가 False일 때
            self.myImage.paste(images[self.image_index], (x_coordinate, 50), images[self.image_index])
            self.joystick.disp.image(self.myImage)
            self.image_index = (self.image_index + 1) % len(images)  # 다음 이미지로 인덱스를 변경
            x_coordinate += 10  # 이미지를 오른쪽으로 이동
            time.sleep(0.1)  # 이미지 전환 속도를 조절하는 데 사용

class SpringMove:
    joystick = Joystick()
    image_loader = ImageLoader()

    eggChick_move_list = [image_loader.get_image("eggChickMove1"), image_loader.get_image("eggChickMove2")]

    while True:
        if joystick.button_L.value == False:  # L 버튼이 눌렸을 때
            switch_images(eggChick_move_list, mirror=True)
        elif joystick.button_R.value == False:  # R 버튼이 눌렸을 때
            switch_images(eggChick_move_list, mirror=False)