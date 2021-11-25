class Hero:

    def __init__(self, name):
        self.name = name
        self.health = 50

class Hero_intelligent(Hero):
    
    # This is not okay because call the same block with other class
    def __init__(self, name):
        self.name = name
        self.health = 100

class Hero_strength(Hero):
    
    # This is not okay because call the same block with other class
    def __init__(self, name):
        self.name = name
        self.health = 200

lina = Hero('lina')
techies = Hero_intelligent('techies')
axe = Hero_strength('axe')

print(lina.__dict__)
print(techies.__dict__)
print(axe.__dict__)
