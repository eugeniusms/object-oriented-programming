class Hero():

    def __init__(self, name, health, armor):
        self.__name = name
        self.__health = health
        self.__armor = armor
        self.info = "name : {}\n\thealth : {}".format(self.__name, self.__health)

    def getHealth(self):
        return self.__health

sniper = Hero("sniper", 100, 10)

print(sniper.info)
