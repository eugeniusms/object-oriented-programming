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


# Initiation object
sniper = Hero("sniper", 100, 10)

# Change the name of object info
print(sniper.info)
sniper.name = "dadang"
print(sniper.info)

# Getter for armor
print(sniper.armor)
print(sniper.__dict__)
# Setter for armor (just like a variable), now we can change the private variable
sniper.armor = 50
print(sniper.armor)
print(sniper.__dict__)
