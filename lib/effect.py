from copy import deepcopy  

class Effect:
    def __init__(self, kind, beforeDamage=False, deathblow=False):
        # Options: heal, buff, freeze, summon, slow, speed crit, nerf, chain, spellDamage
        self.kind = kind
        self.beforeDamage = beforeDamage
        self.deathblow = deathblow
    
    def setEffect(self, fn):
        self.fn = fn
    
    def updateBeforeDamage(self, board):
        if     self.beforeDamage and not self.deathblow: self.fn(board)
    def updateAfterDamage(self, board):
        if not self.beforeDamage and not self.deathblow: self.fn(board)
    def updateDeathblow(self, board):
        if self.deathblow: self.fn(board)
            
    def copy(self):
        return deepcopy(self)