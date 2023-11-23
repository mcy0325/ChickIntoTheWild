from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np
import time
from colorsys import hsv_to_rgb
from Joystick import Joystick
from Egg import Egg
from ImageLoader import ImageLoader

def main():
    #Initialize Joystick
    joystick = Joystick()
    image_loader = ImageLoader()
    
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    joystick.disp.image(my_image)

    #게임 시작 화면
    def GameStart():
        #게임 시작 화면 이미지 리스트
        start_image_list = [image_loader.get_image("gameStart"), image_loader.get_image("gameStory1"), image_loader.get_image("gameStory2")]
        image_index = 0
        
        #게임 시작 화면 이미지 출력
        while True:
            my_image.paste(start_image_list[image_index], (0,0))
            joystick.disp.image(my_image)

            if joystick.button_A.value == False:
                if image_index == len(start_image_list) - 1:
                    break

                image_index += 1

                time.sleep(0.2)
    
    #게임 오버 화면
    def GameOver():
        my_image.paste(image_loader.get_image("gameOver"), (0,0), image_loader.get_image("gameOver"))
        joystick.disp.image(my_image)

        while True:
            if joystick.button_B.value == False:
                GameStart()
                break
            time.sleep(0.2)
    
    #게임 클리어 화면
    #def GameClear():

    GameStart()

    #게임 진행 화면
    if joystick.button_A.value == False:
        my_image.paste(image_loader.get_image("eggBreak"), (0,0), image_loader.get_image("eggBreak"))
        my_image.paste(image_loader.get_image("egg1"), (60,50), image_loader.get_image("egg1"))
        joystick.disp.image(my_image)
        time.sleep(0.2)
        egg_image_list = [image_loader.get_image("egg2"), image_loader.get_image("egg3"), image_loader.get_image("egg4"), image_loader.get_image("egg5"), image_loader.get_image("egg6")]
        egg = Egg(joystick, my_image, egg_image_list)
        egg_success = egg.start()

        if not egg_success:
            GameOver()


if __name__ == '__main__':
    main()
    