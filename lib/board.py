from copy import deepcopy
from hashlib import sha256

class Board:
    def __init__(self):
        self.log = []
        self.mercDict = {} # merc-ID : merc-class-object
        self.teamDict{} # merc-ID : (1,2)
        self.allMercs = []
    
    def addMerc(self, team, merc):
        mercID = sha256((merc.name + str(team)).encode('utf-8')).hexdigest()
        merc.ID = mercID
        self.mercDict[mercID] = merc
        self.teamDict[mercID] = 2 - (int(team)==1)
        self.allMercs.append(merc)
    
    def heal(self, healerID, amount, healeeID=None, healAllTeam=False, condition=None):
        activeTeamIDs = [m.ID for for m in self._active_team(self.teamDict[healerID])]
        
        if healAllTeam:
            for ID in activeTeamIDs:
                self.heal(healerID, amount, ID)
        elif condition is not None:
            for ID in [ID for ID in activeTeamIDs if condition(self.mercDict[ID])]:
                self.heal(healerID, amount, ID)
        else:
            if healeeID is None: healeeID = healerID
            self.mercDict[healeeID].heal(amount)
            
    def buff(self, bufferID, atk=0, HP=0, buffeeID=None, buffAllTeam=False, condition=None):
        activeTeamIDs = [m.ID for for m in self._active_team(self.teamDict[healerID])]
        
        if buffAllTeam:
            for ID in activeTeamIDs:
                self.buff(bufferID, atk, HP, ID)
        elif condition is not None:
            for ID in [ID for ID in activeTeamIDs if condition(self.mercDict[ID])]:
                self.buff(bufferID, atk, HP, ID)
        else:
            if buffeeID is None: buffeeID = bufferID
            self.mercDict[buffeeID].buff(atk, HP)
        

    def _active_team(self, teamNum):
        return [m for ID,m in self.mercDict.items() if self.teamDict[ID] == teamNum and m.active]
    
    def copy(self):
        return deepcopy(self)