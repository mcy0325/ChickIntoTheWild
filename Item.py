import random

class Item:
    def __init__(self, my_image, width, height, item_image):
        self.my_image = my_image
        self.image = item_image
        image_width, image_height = self.image.size
        self.radius = 8
        #아이템 위치 화면 내에서 랜덤으로 설정
        self.position = [random.randint(10, width - image_width), random.randint(10, height - image_height)]

    #아이템 화면에 표시 함수
    def display(self):
        position = [int(p) for p in self.position] 
        self.my_image.paste(self.image, tuple(position), self.image)

    #아이템 위치 반환 함수
    def get_position(self):
        return self.position