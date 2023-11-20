from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np
import time
from colorsys import hsv_to_rgb
from Joystick import Joystick
from Egg import Egg

def main():
    #Initialize Joystick
    joystick = Joystick()
    

    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    joystick.disp.image(my_image)

    #Open Background Images
    img_spring = Image.open('./images/Spring.PNG', mode='r').convert('RGBA')
    img_summer = Image.open('./images/Summer.PNG', mode='r').convert('RGBA')
    img_fall = Image.open('./images/Fall.PNG', mode='r').convert('RGBA')
    img_winter = Image.open('./images/Winter.PNG', mode='r').convert('RGBA')
    img_gameStart = Image.open('./images/GameStart.PNG', mode='r').convert('RGBA')
    img_gameOver = Image.open('./images/GameOver.PNG', mode='r').convert('RGBA')
    img_gameEnd = Image.open('./images/GameEnd.PNG', mode='r').convert('RGBA')
    img_gameStory1 = Image.open('./images/GameStory1.PNG', mode='r').convert('RGBA')
    img_gameStory2 = Image.open('./images/GameStory2.PNG', mode='r').convert('RGBA')
    img_howPlayS = Image.open('./images/HowPlayS.PNG', mode='r').convert('RGBA')
    img_howPlayF = Image.open('./images/HowPlayF.PNG', mode='r').convert('RGBA')
    img_scoreBoard = Image.open('./images/ScoreBoard.PNG', mode='r').convert('RGBA')
    img_growUp = Image.open('./images/GrowUp.PNG', mode='r').convert('RGBA')
    img_eggBreak = Image.open('./images/EggBreak.PNG', mode='r').convert('RGBA')
    img_groundGray1 = Image.open('./images/GroundGray1.PNG', mode='r').convert('RGBA')
    img_groundGray2 = Image.open('./images/GroundGray2.PNG', mode='r').convert('RGBA')
    img_groundGray3 = Image.open('./images/GroundGray3.PNG', mode='r').convert('RGBA')
    img_groundGreen1 = Image.open('./images/GroundGreen1.PNG', mode='r').convert('RGBA')
    img_groundGreen2 = Image.open('./images/GroundGreen2.PNG', mode='r').convert('RGBA')
    img_groundGreen3 = Image.open('./images/GroundGreen3.PNG', mode='r').convert('RGBA')
    img_groundOrange1 = Image.open('./images/GroundOrange1.PNG', mode='r').convert('RGBA')
    img_groundOrange2 = Image.open('./images/GroundOrange2.PNG', mode='r').convert('RGBA')
    img_groundOrange3 = Image.open('./images/GroundOrange3.PNG', mode='r').convert('RGBA')
    img_groundPink1 = Image.open('./images/GroundPink1.PNG', mode='r').convert('RGBA')
    img_groundPink2 = Image.open('./images/GroundPink2.PNG', mode='r').convert('RGBA')
    img_groundPink3 = Image.open('./images/GroundPink3.PNG', mode='r').convert('RGBA')
    img_ladder = Image.open('./images/Ladder.PNG', mode='r').convert('RGBA')

    #Open Character Images
    img_bigRooster = Image.open('./images/BigRooster.PNG', mode='r').convert('RGBA')
    img_chick = Image.open('./images/Chick.PNG', mode='r').convert('RGBA')
    img_eggChick = Image.open('./images/EggChick.PNG', mode='r').convert('RGBA')
    img_rooster = Image.open('./images/Rooster.PNG', mode='r').convert('RGBA')
    
    #Open Egg Images
    img_egg1 = Image.open('./images/Egg1.PNG', mode='r').convert('RGBA')
    img_egg2 = Image.open('./images/Egg2.PNG', mode='r').convert('RGBA')
    img_egg3 = Image.open('./images/Egg3.PNG', mode='r').convert('RGBA')
    img_egg4 = Image.open('./images/Egg4.PNG', mode='r').convert('RGBA')
    img_egg5 = Image.open('./images/Egg5.PNG', mode='r').convert('RGBA')
    img_egg6 = Image.open('./images/Egg6.PNG', mode='r').convert('RGBA')

    #Open Item Images
    img_bud = Image.open('./images/Bud.PNG', mode='r').convert('RGBA')
    img_cherry = Image.open('./images/Cherry.PNG', mode='r').convert('RGBA')
    img_flag = Image.open('./images/Flag.PNG', mode='r').convert('RGBA')
    img_heart = Image.open('./images/Heart.PNG', mode='r').convert('RGBA')
    img_ice = Image.open('./images/Ice.PNG', mode='r').convert('RGBA')
    img_waterDrop = Image.open('./images/WaterDrop.PNG', mode='r').convert('RGBA')

    #Open Obstacle Images
    img_obstacle1 = Image.open('./images/Obstacle1.PNG', mode='r').convert('RGBA')
    img_obstacle2 = Image.open('./images/Obstacle2.PNG', mode='r').convert('RGBA')

    #Open Enemy Images
    img_bomb = Image.open('./images/Bomb.PNG', mode='r').convert('RGBA')
    img_bombDie = Image.open('./images/BombDie.PNG', mode='r').convert('RGBA')
    img_snowman = Image.open('./images/Snowman.PNG', mode='r').convert('RGBA')
    img_snowmanDie = Image.open('./images/SnowmanDie.PNG', mode='r').convert('RGBA')

    #Open Character Move Images
    img_bigRoosterMove1 = Image.open('./images/BigRoosterMove1.PNG', mode='r').convert('RGBA')
    img_bigRoosterMove2 = Image.open('./images/BigRoosterMove2.PNG', mode='r').convert('RGBA')
    img_brAttack1 = Image.open('./images/BrAttack1.PNG', mode='r').convert('RGBA')
    img_brAttack2 = Image.open('./images/BrAttack2.PNG', mode='r').convert('RGBA')
    img_chickBehind = Image.open('./images/ChickBehind.PNG', mode='r').convert('RGBA')
    img_chickMove1 = Image.open('./images/ChickMove1.PNG', mode='r').convert('RGBA')
    img_chickMove2 = Image.open('./images/ChickMove2.PNG', mode='r').convert('RGBA')
    img_eggChickBehind = Image.open('./images/EggChickBehind.PNG', mode='r').convert('RGBA')
    img_eggChickMove1 = Image.open('./images/EggChickMove1.PNG', mode='r').convert('RGBA')
    img_eggChickMove2 = Image.open('./images/EggChickMove2.PNG', mode='r').convert('RGBA')
    img_rainbowBehind = Image.open('./images/RainbowBehind.PNG', mode='r').convert('RGBA')
    img_rainbowBrMove1 = Image.open('./images/RainbowBrMove1.PNG', mode='r').convert('RGBA')
    img_rainbowBrMove2 = Image.open('./images/RainbowBrMove2.PNG', mode='r').convert('RGBA')
    img_rainbowMove1 = Image.open('./images/RainbowMove1.PNG', mode='r').convert('RGBA')
    img_rainbowMove2 = Image.open('./images/RainbowMove2.PNG', mode='r').convert('RGBA')
    img_roosterAttack1 = Image.open('./images/RoosterAttack1.PNG', mode='r').convert('RGBA')
    img_roosterAttack2 = Image.open('./images/RoosterAttack2.PNG', mode='r').convert('RGBA')
    img_roosterBehind = Image.open('./images/RoosterBehind.PNG', mode='r').convert('RGBA')
    img_roosterMove1 = Image.open('./images/RoosterMove1.PNG', mode='r').convert('RGBA')
    img_roosterMove2 = Image.open('./images/RoosterMove2.PNG', mode='r').convert('RGBA')

    #게임 시작 화면
    def GameStart():
        #게임 시작 화면 이미지 리스트
        start_image_list = [img_gameStart, img_gameStory1, img_gameStory2]
        image_index = 0
        
        #게임 시작 화면 이미지 출력
        while True:
            my_image.paste(start_image_list[image_index], (0,0))
            joystick.disp.image(my_image)

            if joystick.button_A.value == False:
                if image_index == len(start_image_list) - 1:
                    break

                image_index += 1

                time.sleep(0.5)
    
    #게임 오버 화면
    #def GameOver():
    
    #게임 클리어 화면
    #def GameClear():


    GameStart()

    #게임 진행 화면
    if joystick.button_A.value == False:
        my_image.paste(img_eggBreak, (0,0), img_eggBreak)
        egg_image_list = [img_egg1, img_egg2, img_egg3, img_egg4, img_egg5, img_egg6]

        egg = Egg(joystick, my_image, egg_image_list)
        egg.start()

        


if __name__ == '__main__':
    main()
    