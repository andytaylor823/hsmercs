from copy import deepcopy

class Ability:
    def __init__(self, name, ix, speed, cooldown=0):
        self.name = name
        self.ix = ix
        self.baseSpeed = speed
        self.effects = []
        self.cooldown = cooldown
        
    def setSchool(self, school):
        # Options are: fire, frost, nature, fel, shadow, holy
        self.school = school
    
    def setDamage(self, dealsDamage=False, attack=False, baseDamage=0, conditionDamage=None, ignoresTaunt=False):
        # T/F if the ability deals damage or not
        self.dealsDamage = dealsDamage
        
        # If deals damage by attacking and if ignores taunt
        self.attack, self.ignoresTaunt = attack, ignoresTaunt
        
        # Integer base damage, only if dealsDamage and not attack
        self.baseDamage = baseDamage
        
        # Function which takes in board as arg and returns....something
        self.conditionDamage = conditionDamage
    
    def setDesc(self, desc):
        self.desc = desc
    
    def addEffect(self, effect):
        self.effects.append(effect)

    def copy(self):
        return deepcopy(self)
