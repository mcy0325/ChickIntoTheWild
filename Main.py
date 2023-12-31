from Game import Game
from Joystick import Joystick
from ImageLoader import ImageLoader
from PIL import Image

#메인 함수
def main():
    joystick = Joystick()
    image_loader = ImageLoader()

    my_image = Image.new("RGB", (joystick.width, joystick.height))
    joystick.disp.image(my_image)

    #게임 객체 생성
    game = Game(joystick, image_loader)
    #게임 시작
    game.start(my_image)

if __name__ == '__main__':
    main()
