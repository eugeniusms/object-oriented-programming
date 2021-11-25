class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

class Hero_intelligent(Hero):
    
    def __init__(self, name):
        Hero.__init__(self, name, 100)

class Hero_strength(Hero):
    
    def __init__(self, name):
        Hero.__init__(self,name, 200)

techies = Hero_intelligent('techies')
axe = Hero_strength('axe')

print(techies.__dict__)
print(axe.__dict__)
