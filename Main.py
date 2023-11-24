from Game import Game
from Joystick import Joystick
from ImageLoader import ImageLoader
from PIL import Image, ImageDraw

def main():
    joystick = Joystick()
    image_loader = ImageLoader()

    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    joystick.disp.image(my_image)

    game = Game(joystick, image_loader, my_image)
    game.start()

if __name__ == '__main__':
    main()