class Hero:

    # Private class variable
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {} : \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {} \n\t".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attPower, self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, 'level up')
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def kill(self, enemy):
        self.gainExp = 50


necron = Hero("necron", 100, 5, 10)
minion = Hero("minion", 10, 5, 5)
print(necron.info)

necron.gainExp = 50
necron.gainExp = 80 # Necron level up to level 2
print(necron.info)
print(necron.__dict__)

# If necron kill many minions 50x 3 = 150
necron.kill(minion)
necron.kill(minion) # Necron level up to level 3
necron.kill(minion) 
print(necron.info)
