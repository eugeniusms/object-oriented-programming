class Hero():

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    @property
    def info(self):
        return "name : {}\n\thealth : {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

# Initiation object
sniper = Hero("sniper", 100, 10)

# Change the name of object info
print(sniper.info)
sniper.name = "dadang"
print(sniper.info)

# Getter for armor
print(sniper.armor)
# sniper.armor = 10 >> This makes error because it's private, and getter just for read the contain of sniper.armor not change it
