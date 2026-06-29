class GrandFather:
    def Skill(self):
        print("Reading current affairs")
class Father(GrandFather):
    def FatherSkill(self):
        print("Makes Money")
class Son(Father):
    def SonSkill(self):
        print("1.watching reels\n 2.eating \n 3. sleeping\n 4.studying")

#instance
son=Son()
son.SonSkill()
son.FatherSkill()
son.Skill()
