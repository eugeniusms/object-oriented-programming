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

# But if we replace info with new instantiation, we can do this
sniper.info = "info"
# This is make sniper.info just raise string value "info" because self.info occur like a variable
print(sniper.info)
