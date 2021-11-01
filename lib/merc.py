from copy import deepcopy

class Merc:
    def __init__(self, name, color=None):
        self.name = name
        self.abilities = []
        self.color = color
        self.active = False
        self.dead = False
        self.taunt, self.tauntCounter = False, 0
        self.frozen, self.frozenCounter = False, 0
        self.equipmentName = ''
    
    def setRace(self, race):
        self.race = race
    
    def setStats(self, maxHP, atk):
        self.og_maxHP, self.maxHP = maxHP, maxHP
        self.og_atk, self.atk = atk, atk
        self.currentHP = maxHP
        self.atkBuff, self.HPBuff = 0,0
        
    def assignAbility(self, ability):
        self.abilities.append(ability)
        self.abilities.sort(key = lambda a: a.ix)
        
    def heal(self, amount):
        self.currentHP = min(self.maxHP, self.currentHP + amount)
    
    def buff(self, atk, HP):
        self.atk += atk
        self.currentHP += HP
        self.maxHP += HP

    
    def copy(self):
        return deepcopy(self)
    
    def __str__(self):
        line = self.name + ' %i / %i\n' %(self.atk, self.currentHP)
        for i, a in enumerate(self.abilities):
            line += '\t%i.) %s Speed=%i ' %(i, a.name)
            if a.cooldown > 0: line += '(Cooldown=%i)' %a.cooldown
            line += '\n\t\t' + (a.desc(self) if callable(a) else a.desc) + '\n'
        if self.taunt: line += 'Taunt for %i turns\n' %self.tauntCounter
        if self.frozen: line += 'Frozen for %i turns\n' %self.frozenCounter
        return line[:-1] # take off final \n char