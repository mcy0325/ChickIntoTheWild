from PIL import Image

class ImageLoader:
    def __init__(self):
        self.images = self.load_images()

    def load_images(self):
        #Open Background Images
        img_spring = Image.open('./images/Spring.PNG', mode='r').convert('RGBA')
        img_summer = Image.open('./images/Summer.PNG', mode='r').convert('RGBA')
        img_fall = Image.open('./images/Fall.PNG', mode='r').convert('RGBA')
        img_winter = Image.open('./images/Winter.PNG', mode='r').convert('RGBA')
        img_gameStart = Image.open('./images/GameStart.PNG', mode='r').convert('RGBA')
        img_gameOver = Image.open('./images/GameOver.PNG', mode='r').convert('RGBA')
        img_gameEnd = Image.open('./images/GameEnd.PNG', mode='r').convert('RGBA')
        img_gameStory1 = Image.open('./images/GameStory1.PNG', mode='r').convert('RGBA')
        img_gameStory2 = Image.open('./images/GameStory2.PNG', mode='r').convert('RGBA')
        img_howPlayS = Image.open('./images/HowPlayS.PNG', mode='r').convert('RGBA')
        img_howPlayF = Image.open('./images/HowPlayF.PNG', mode='r').convert('RGBA')
        img_scoreBoard = Image.open('./images/ScoreBoard.PNG', mode='r').convert('RGBA')
        img_growUp = Image.open('./images/GrowUp.PNG', mode='r').convert('RGBA')
        img_eggBreak = Image.open('./images/EggBreak.PNG', mode='r').convert('RGBA')
        img_groundGray1 = Image.open('./images/GroundGray1.PNG', mode='r').convert('RGBA')
        img_groundGray2 = Image.open('./images/GroundGray2.PNG', mode='r').convert('RGBA')
        img_groundGray3 = Image.open('./images/GroundGray3.PNG', mode='r').convert('RGBA')
        img_groundGreen1 = Image.open('./images/GroundGreen1.PNG', mode='r').convert('RGBA')
        img_groundGreen2 = Image.open('./images/GroundGreen2.PNG', mode='r').convert('RGBA')
        img_groundGreen3 = Image.open('./images/GroundGreen3.PNG', mode='r').convert('RGBA')
        img_groundOrange1 = Image.open('./images/GroundOrange1.PNG', mode='r').convert('RGBA')
        img_groundOrange2 = Image.open('./images/GroundOrange2.PNG', mode='r').convert('RGBA')
        img_groundOrange3 = Image.open('./images/GroundOrange3.PNG', mode='r').convert('RGBA')
        img_groundPink1 = Image.open('./images/GroundPink1.PNG', mode='r').convert('RGBA')
        img_groundPink2 = Image.open('./images/GroundPink2.PNG', mode='r').convert('RGBA')
        img_groundPink3 = Image.open('./images/GroundPink3.PNG', mode='r').convert('RGBA')
        img_ladder = Image.open('./images/Ladder.PNG', mode='r').convert('RGBA')

        #Open Character Images
        img_bigRooster = Image.open('./images/BigRooster.PNG', mode='r').convert('RGBA')
        img_chick = Image.open('./images/Chick.PNG', mode='r').convert('RGBA')
        img_eggChick = Image.open('./images/EggChick.PNG', mode='r').convert('RGBA')
        img_rooster = Image.open('./images/Rooster.PNG', mode='r').convert('RGBA')
        
        #Open Egg Images
        img_egg1 = Image.open('./images/Egg1.PNG', mode='r').convert('RGBA')
        img_egg2 = Image.open('./images/Egg2.PNG', mode='r').convert('RGBA')
        img_egg3 = Image.open('./images/Egg3.PNG', mode='r').convert('RGBA')
        img_egg4 = Image.open('./images/Egg4.PNG', mode='r').convert('RGBA')
        img_egg5 = Image.open('./images/Egg5.PNG', mode='r').convert('RGBA')
        img_egg6 = Image.open('./images/Egg6.PNG', mode='r').convert('RGBA')

        #Open Item Images
        img_bud = Image.open('./images/Bud.PNG', mode='r').convert('RGBA')
        img_cherry = Image.open('./images/Cherry.PNG', mode='r').convert('RGBA')
        img_flag = Image.open('./images/Flag.PNG', mode='r').convert('RGBA')
        img_heart = Image.open('./images/Heart.PNG', mode='r').convert('RGBA')
        img_ice = Image.open('./images/Ice.PNG', mode='r').convert('RGBA')
        img_waterDrop = Image.open('./images/WaterDrop.PNG', mode='r').convert('RGBA')

        #Open Obstacle Images
        img_obstacle1 = Image.open('./images/Obstacle1.PNG', mode='r').convert('RGBA')
        img_obstacle2 = Image.open('./images/Obstacle2.PNG', mode='r').convert('RGBA')

        #Open Enemy Images
        img_bomb = Image.open('./images/Bomb.PNG', mode='r').convert('RGBA')
        img_bombDie = Image.open('./images/BombDie.PNG', mode='r').convert('RGBA')
        img_snowman = Image.open('./images/Snowman.PNG', mode='r').convert('RGBA')
        img_snowmanDie = Image.open('./images/SnowmanDie.PNG', mode='r').convert('RGBA')

        #Open Character Move Images
        img_bigRoosterMove1 = Image.open('./images/BigRoosterMove1.PNG', mode='r').convert('RGBA')
        img_bigRoosterMove2 = Image.open('./images/BigRoosterMove2.PNG', mode='r').convert('RGBA')
        img_brAttack1 = Image.open('./images/BrAttack1.PNG', mode='r').convert('RGBA')
        img_brAttack2 = Image.open('./images/BrAttack2.PNG', mode='r').convert('RGBA')
        img_chickBehind = Image.open('./images/ChickBehind.PNG', mode='r').convert('RGBA')
        img_chickMove1 = Image.open('./images/ChickMove1.PNG', mode='r').convert('RGBA')
        img_chickMove2 = Image.open('./images/ChickMove2.PNG', mode='r').convert('RGBA')
        img_eggChickBehind = Image.open('./images/EggChickBehind.PNG', mode='r').convert('RGBA')
        img_eggChickMove1 = Image.open('./images/EggChickMove1.PNG', mode='r').convert('RGBA')
        img_eggChickMove2 = Image.open('./images/EggChickMove2.PNG', mode='r').convert('RGBA')
        img_rainbowBehind = Image.open('./images/RainbowBehind.PNG', mode='r').convert('RGBA')
        img_rainbowBrMove1 = Image.open('./images/RainbowBrMove1.PNG', mode='r').convert('RGBA')
        img_rainbowBrMove2 = Image.open('./images/RainbowBrMove2.PNG', mode='r').convert('RGBA')
        img_rainbowMove1 = Image.open('./images/RainbowMove1.PNG', mode='r').convert('RGBA')
        img_rainbowMove2 = Image.open('./images/RainbowMove2.PNG', mode='r').convert('RGBA')
        img_roosterAttack1 = Image.open('./images/RoosterAttack1.PNG', mode='r').convert('RGBA')
        img_roosterAttack2 = Image.open('./images/RoosterAttack2.PNG', mode='r').convert('RGBA')
        img_roosterBehind = Image.open('./images/RoosterBehind.PNG', mode='r').convert('RGBA')
        img_roosterMove1 = Image.open('./images/RoosterMove1.PNG', mode='r').convert('RGBA')
        img_roosterMove2 = Image.open('./images/RoosterMove2.PNG', mode='r').convert('RGBA')

        return {
            "spring" : img_spring,
            "summer" : img_summer,
            "fall" : img_fall,
            "winter" : img_winter,
            "gameStart" : img_gameStart,
            "gameOver" : img_gameOver,
            "gameEnd" : img_gameEnd,
            "gameStory1" : img_gameStory1,
            "gameStory2" : img_gameStory2,
            "howPlayS" : img_howPlayS,
            "howPlayF" : img_howPlayF,
            "scoreBoard" : img_scoreBoard,
            "growUp" : img_growUp,
            "eggBreak" : img_eggBreak,
            "groundGray1" : img_groundGray1,
            "groundGray2" : img_groundGray2,
            "groundGray3" : img_groundGray3,
            "groundGreen1" : img_groundGreen1,
            "groundGreen2" : img_groundGreen2,
            "groundGreen3" : img_groundGreen3,
            "groundOrange1" : img_groundOrange1,
            "groundOrange2" : img_groundOrange2,
            "groundOrange3" : img_groundOrange3,
            "groundPink1" : img_groundPink1,
            "groundPink2" : img_groundPink2,
            "groundPink3" : img_groundPink3,
            "ladder" : img_ladder,
            "bigRooster" : img_bigRooster,
            "chick" : img_chick,
            "eggChick" : img_eggChick,
            "rooster" : img_rooster,
            "egg1" : img_egg1,
            "egg2" : img_egg2,
            "egg3" : img_egg3,
            "egg4" : img_egg4,
            "egg5" : img_egg5,
            "egg6" : img_egg6,
            "bud" : img_bud,
            "cherry" : img_cherry,
            "flag" : img_flag,
            "heart" : img_heart,
            "ice" : img_ice,
            "waterDrop" : img_waterDrop,
            "obstacle1" : img_obstacle1,
            "obstacle2" : img_obstacle2,
            "bomb" : img_bomb,
            "bombDie" : img_bombDie,
            "snowman" : img_snowman,
            "snowmanDie" : img_snowmanDie,
            "bigRoosterMove1" : img_bigRoosterMove1,
            "bigRoosterMove2" : img_bigRoosterMove2,
            "brAttack1" : img_brAttack1,
            "brAttack2" : img_brAttack2,
            "chickBehind" : img_chickBehind,
            "chickMove1" : img_chickMove1,
            "chickMove2" : img_chickMove2,
            "eggChickBehind" : img_eggChickBehind,
            "eggChickMove1" : img_eggChickMove1,
            "eggChickMove2" : img_eggChickMove2,
            "rainbowBehind" : img_rainbowBehind,
            "rainbowBrMove1" : img_rainbowBrMove1,
            "rainbowBrMove2" : img_rainbowBrMove2,
            "rainbowMove1" : img_rainbowMove1,
            "rainbowMove2" : img_rainbowMove2,
            "roosterAttack1" : img_roosterAttack1,
            "roosterAttack2" : img_roosterAttack2,
            "roosterBehind" : img_roosterBehind,
            "roosterMove1" : img_roosterMove1,
            "roosterMove2" : img_roosterMove2
        }

    def get_image(self, name):
        return self.images[name]