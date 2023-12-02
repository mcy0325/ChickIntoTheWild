import random

class Enemy:
    def __init__(self, x, y, speed, image, image_loader):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.image_loader = image_loader
        self.radius = 16
        #적의 이동 방향 무작위 설정
        self.direction = random.choice(['up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right'])

    #적의 위치 업데이트 함수
    def update(self):
        #각 방향에 대해 적이 화면 밖으로 나가지 않도록 이동 방향 바꿈
        if self.direction == 'up':
            if self.y - self.speed >= 20:
                self.y -= self.speed
            else:
                self.direction = random.choice(['down', 'left', 'right', 'down-left', 'down-right'])
        elif self.direction == 'down':
            if self.y + self.speed <= 190:
                self.y += self.speed
            else:
                self.direction = random.choice(['up', 'left', 'right', 'up-left', 'up-right'])
        elif self.direction == 'left':
            if self.x - self.speed >= 20:
                self.x -= self.speed
            else:
                self.direction = random.choice(['up', 'down', 'right', 'up-right', 'down-right'])
        elif self.direction == 'right':
            if self.x + self.speed <= 190:
                self.x += self.speed
            else:
                self.direction = random.choice(['up', 'down', 'left', 'up-left', 'down-left'])
        elif self.direction == 'up-left':
            if self.x - self.speed >= 20 and self.y - self.speed >= 20:
                self.x -= self.speed
                self.y -= self.speed
            else:
                self.direction = random.choice(['down', 'right', 'down-right'])
        elif self.direction == 'up-right':
            if self.x + self.speed <= 190 and self.y - self.speed >= 20:
                self.x += self.speed
                self.y -= self.speed
            else:
                self.direction = random.choice(['down', 'left', 'down-left'])
        elif self.direction == 'down-left':
            if self.x - self.speed >= 20 and self.y + self.speed <= 190:
                self.x -= self.speed
                self.y += self.speed
            else:
                self.direction = random.choice(['up', 'right', 'up-right'])
        elif self.direction == 'down-right':
            if self.x + self.speed <= 190 and self.y + self.speed <= 190:
                self.x += self.speed
                self.y += self.speed
            else:
                self.direction = random.choice(['up', 'left', 'up-left'])

    # 적 이미지 화면에 표시하는 함수
    def draw(self, my_image):
        my_image.paste(self.image_loader.get_image(self.image), (self.x, self.y), self.image_loader.get_image(self.image))

    # 적의 위치 반환 함수
    def get_position(self):
        return self.x, self.y
