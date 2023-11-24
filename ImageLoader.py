from PIL import Image

class ImageLoader:
    def __init__(self):
        self.images = self.load_images()

    def load_images(self):
        #Open Background Images
        img_eggBreak = Image.open('./images/eggBreak.PNG', mode='r').convert('RGBA')
        img_fall = Image.open('./images/fall.PNG', mode='r').convert('RGBA')
        img_gameEnd = Image.open('./images/gameEnd.PNG', mode='r').convert('RGBA')
        img_gameOver = Image.open('./images/gameOver.PNG', mode='r').convert('RGBA')
        img_gameStart = Image.open('./images/gameStart.PNG', mode='r').convert('RGBA')
        img_gameStory1 = Image.open('./images/gameStory1.PNG', mode='r').convert('RGBA')
        img_gameStory2 = Image.open('./images/gameStory2.PNG', mode='r').convert('RGBA')
        img_growUp = Image.open('./images/growUp.PNG', mode='r').convert('RGBA')
        img_spring = Image.open('./images/spring.PNG', mode='r').convert('RGBA')
        img_summer = Image.open('./images/summer.PNG', mode='r').convert('RGBA')
        img_winter = Image.open('./images/winter.PNG', mode='r').convert('RGBA')
        img_totalScore = Image.open('./images/totalScore.PNG', mode='r').convert('RGBA')

        #Open Character Images
        img_chick = Image.open('./images/chick.PNG', mode='r').convert('RGBA')
        img_eggChick = Image.open('./images/eggChick.PNG', mode='r').convert('RGBA')
        img_goodRooster = Image.open('./images/goodRooster.PNG', mode='r').convert('RGBA')
        img_greatRooster = Image.open('./images/greatRooster.PNG', mode='r').convert('RGBA')
        img_rooster = Image.open('./images/rooster.PNG', mode='r').convert('RGBA')
        
        #Open Character Heart Image
        img_heart = Image.open('./images/heart.PNG', mode='r').convert('RGBA')

        #Open Egg Images
        img_egg1 = Image.open('./images/egg1.PNG', mode='r').convert('RGBA')
        img_egg2 = Image.open('./images/egg2.PNG', mode='r').convert('RGBA')
        img_egg3 = Image.open('./images/egg3.PNG', mode='r').convert('RGBA')
        img_egg4 = Image.open('./images/egg4.PNG', mode='r').convert('RGBA')
        img_egg5 = Image.open('./images/egg5.PNG', mode='r').convert('RGBA')
        img_egg6 = Image.open('./images/egg6.PNG', mode='r').convert('RGBA')

        #Open Item Images
        img_apple = Image.open('./images/apple.PNG', mode='r').convert('RGBA')
        img_bud = Image.open('./images/bud.PNG', mode='r').convert('RGBA')
        img_flag = Image.open('./images/flag.PNG', mode='r').convert('RGBA')
        img_ice = Image.open('./images/ice.PNG', mode='r').convert('RGBA')
        img_waterDrop = Image.open('./images/waterDrop.PNG', mode='r').convert('RGBA')

        #Open Enemy Images
        img_butterfly = Image.open('./images/butterfly.PNG', mode='r').convert('RGBA')
        img_cloud = Image.open('./images/cloud.PNG', mode='r').convert('RGBA')
        img_sharp = Image.open('./images/sharp.PNG', mode='r').convert('RGBA')
        img_worm = Image.open('./images/worm.PNG', mode='r').convert('RGBA')

        #Open Character Move Images
        img_bigSpecialMove1 = Image.open('./images/bigSpecialMove1.PNG', mode='r').convert('RGBA')
        img_bigSpecialMove2 = Image.open('./images/bigSpecialMove2.PNG', mode='r').convert('RGBA')
        img_chickMove1 = Image.open('./images/chickMove1.PNG', mode='r').convert('RGBA')
        img_chickMove2 = Image.open('./images/chickMove2.PNG', mode='r').convert('RGBA')
        img_eggChickMove1 = Image.open('./images/eggChickMove1.PNG', mode='r').convert('RGBA')
        img_eggChickMove2 = Image.open('./images/eggChickMove2.PNG', mode='r').convert('RGBA')
        img_goodRoosterMove1 = Image.open('./images/goodRoosterMove1.PNG', mode='r').convert('RGBA')
        img_goodRoosterMove2 = Image.open('./images/goodRoosterMove2.PNG', mode='r').convert('RGBA')
        img_roosterMove1 = Image.open('./images/roosterMove1.PNG', mode='r').convert('RGBA')
        img_roosterMove2 = Image.open('./images/roosterMove2.PNG', mode='r').convert('RGBA')
        img_specialMove1 = Image.open('./images/specialMove1.PNG', mode='r').convert('RGBA')
        img_specialMove2 = Image.open('./images/specialMove2.PNG', mode='r').convert('RGBA')

        return {
            "eggBreak": img_eggBreak,
            "fall": img_fall,
            "gameEnd": img_gameEnd,
            "gameOver": img_gameOver,
            "gameStart": img_gameStart,
            "gameStory1": img_gameStory1,
            "gameStory2": img_gameStory2,
            "growUp": img_growUp,
            "spring": img_spring,
            "summer": img_summer,
            "winter": img_winter,
            "totalScore": img_totalScore,
            "chick": img_chick,
            "eggChick": img_eggChick,
            "goodRooster": img_goodRooster,
            "greatRooster": img_greatRooster,
            "rooster": img_rooster,
            "heart": img_heart,
            "egg1": img_egg1,
            "egg2": img_egg2,
            "egg3": img_egg3,
            "egg4": img_egg4,
            "egg5": img_egg5,
            "egg6": img_egg6,
            "apple": img_apple,
            "bud": img_bud,
            "flag": img_flag,
            "ice": img_ice,
            "waterDrop": img_waterDrop,
            "butterfly": img_butterfly,
            "cloud": img_cloud,
            "sharp": img_sharp,
            "worm": img_worm,
            "bigSpecialMove1": img_bigSpecialMove1,
            "bigSpecialMove2": img_bigSpecialMove2,
            "chickMove1": img_chickMove1,
            "chickMove2": img_chickMove2,
            "eggChickMove1": img_eggChickMove1,
            "eggChickMove2": img_eggChickMove2,
            "goodRoosterMove1": img_goodRoosterMove1,
            "goodRoosterMove2": img_goodRoosterMove2,
            "roosterMove1": img_roosterMove1,
            "roosterMove2": img_roosterMove2,
            "specialMove1": img_specialMove1,
            "specialMove2": img_specialMove2
        }

    def get_image(self, name):
        return self.images[name]