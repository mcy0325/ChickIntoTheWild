import random
from Joystick import Joystick

class Enemy:
    def __init__(self, x, y, speed, image, image_loader):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.image_loader = image_loader
        self.direction = random.choice(['up', 'down', 'left', 'right'])

    def update(self):
        if self.direction == 'up':
            self.y -= self.speed
            if self.y <= 20:
                self.direction = random.choice(['down', 'left', 'right'])
        elif self.direction == 'down':
            self.y += self.speed
            if self.y >= 190:
                self.direction = random.choice(['up', 'left', 'right'])
        elif self.direction == 'left':
            self.x -= self.speed
            if self.x <= 20:
                self.direction = random.choice(['up', 'down', 'right'])
        elif self.direction == 'right':
            self.x += self.speed
            if self.x >= 190:
                self.direction = random.choice(['up', 'down', 'left'])

    def draw(self, my_image):
        my_image.paste(self.image_loader.get_image(self.image), (self.x, self.y), self.image_loader.get_image(self.image))
        
    def get_position(self):
        return self.x, self.y
