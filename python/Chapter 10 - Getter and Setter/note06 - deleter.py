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

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('armor didelete')
        self.__armor = None

# Initiation object
sniper = Hero("sniper", 100, 10)

# Change the name of object info
print(sniper.info)
sniper.name = "dadang"
print(sniper.info)

# Getter for armor
print(sniper.armor)
print(sniper.__dict__)

# Setter for armor (just like a variable)
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)

# Deleter for armor, we can del the variable that makes this program get less memory
del sniper.armor
print(sniper.__dict__)
