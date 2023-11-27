import time
from PIL import ImageOps

class Character:
    def __init__(self, width, height, image1, image2, my_image, joystick, image_loader):
        self.state = None
        self.images = [image1, image2]
        self.current_image = self.images[0]
        self.my_image = my_image
        self.joystick = joystick
        self.image_loader = image_loader
        image_width, image_height = self.current_image.size
        self.position = [width / 2 - image_width / 2, height / 2 - image_height / 2, width / 2 + image_width / 2, height / 2 + image_height / 2]
        self.last_updated = time.time()
        self.flip = False

    def move(self, command=None):
        if command['up_pressed'] or command['down_pressed'] or command['left_pressed'] or command['right_pressed']:
            if command['up_pressed']:
                self.position[1] = max(0, self.position[1] - 5)
                self.position[3] = max(self.position[1] + self.current_image.size[1], self.position[3] - 5)
            if command['down_pressed']:
                self.position[1] = min(self.my_image.size[1] - self.current_image.size[1], self.position[1] + 5)
                self.position[3] = min(self.my_image.size[1], self.position[3] + 5)
            if command['left_pressed']:
                self.position[0] = max(0, self.position[0] - 5)
                self.position[2] = max(self.position[0] + self.current_image.size[0], self.position[2] - 5)
                self.flip = True
            if command['right_pressed']:
                self.position[0] = min(self.my_image.size[0] - self.current_image.size[0], self.position[0] + 5)
                self.position[2] = min(self.my_image.size[0], self.position[2] + 5)
                self.flip = False

            if time.time() - self.last_updated > 0.1:  # 0.1초마다 이미지를 전환합니다.
                if self.current_image == self.images[0]:
                    self.current_image = self.images[1]
                else:
                    self.current_image = self.images[0]
                self.last_updated = time.time()


    def display(self):
        position = [int(p) for p in self.position]

        if self.flip:
            current_image = ImageOps.mirror(self.current_image)
        else:
            current_image = self.current_image

        current_image = current_image.resize((position[2] - position[0], position[3] - position[1]))

        self.my_image.paste(current_image, tuple(position), current_image)
        self.joystick.disp.image(self.my_image)

    
    def get_position(self):
        x1, y1, x2, y2 = self.position
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        return center_x, center_y

