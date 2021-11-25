class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health: {}".format(self.name, self.health))

class Hero_intelligent(Hero):
    
    def __init__(self, name):
        # Hero.__init__(self, name, 100)
        super().__init__(name, 100)
        super().showInfo()

class Hero_strength(Hero):
    
    def __init__(self, name):
        super().__init__(name, 200)
        super().showInfo()


techies = Hero_intelligent('techies')
axe = Hero_strength('axe')
