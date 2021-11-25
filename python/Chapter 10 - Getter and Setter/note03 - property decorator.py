class Hero():

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    @property
    def info(self):
        return "name : {}\n\thealth : {}".format(self.name, self.__health)

sniper = Hero("sniper", 100, 10)

print(sniper.info)

# With @property decorator, this info can change everytime, we can change object name (in public variable) in runtime
# Also the other constructor keep private :D
sniper.name = "dadang"

print(sniper.info)
