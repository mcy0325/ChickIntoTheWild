import random
from PIL import Image

class Item:
    def __init__(self, my_image, width, height, item_image):
        self.my_image = my_image
        self.image = item_image
        image_width, image_height = self.image.size
        self.position = [random.randint(0, width - image_width), random.randint(0, height - image_height)]

    def display(self):
        position = [int(p) for p in self.position]  # position의 각 요소를 정수로 변환
        mask = Image.new('L', self.image.size, color=255)  # 아이템 이미지와 같은 크기의 새 마스크 생성
        self.my_image.paste(self.image, tuple(position), self.image)  # 마스크 사용
