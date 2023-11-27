import random

class Item:
    def __init__(self, my_image, width, height, item_image):
        self.my_image = my_image
        self.image = item_image
        image_width, image_height = self.image.size
        self.position = [random.randint(0, width - image_width), random.randint(0, height - image_height)]

    def display(self):
        position = [int(p) for p in self.position]  # position의 각 요소를 정수로 변환
        self.my_image.paste(self.image, tuple(position), self.image)

    def get_position(self):
        return self.position
