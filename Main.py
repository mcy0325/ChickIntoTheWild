from Game import Game
from Joystick import Joystick
from ImageLoader import ImageLoader
from PIL import Image

def main():
    joystick = Joystick()
    image_loader = ImageLoader()

    my_image = Image.new("RGB", (joystick.width, joystick.height))
    joystick.disp.image(my_image)

    game = Game(joystick, image_loader)
    game.start(my_image)

if __name__ == '__main__':
    main()

#무적 기능 추가해야함
#egg stage 시간 출력해야함
#장애물 대각선으로도 움직일 수 있게 하고 싶음
#이미지 수정 해야함 버튼 누르라고 하는거 지워버려 growUp화면에서 totalScore에도 있을걸 찾아봐
#이것만 대충 수정하면은 임베 끝날듯