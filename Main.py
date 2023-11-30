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
