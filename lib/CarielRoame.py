from merc import Merc
from ability import Ability
from effect import Effect

#################
#               #
#               #
#  Define Merc  #
#               #
#               #
#################
carielRoame = Merc('Cariel Roame', color='red')
carielRoame.setRace('Human')
carielRoame.setStats(10, 67)

#################
#               #
# First Ability #
#               #
#################
carielRoameAbility1 = Ability('Crusader\'s Blow', 1, 6)
carielRoameAbility1.setDamage(dealsDamage=True, isAttack=True)

################
# First Effect #
################
carielRoameAbility1Effect1 = Effect('heal', deathblow=True)
def carielRoameAbility1Effect1Update(board, actor, target=None):
    board.heal(actor.ID, 40, healAllTeam=(actor.equipmentName.lower()=='hammer of dawn'))
carielRoameAbility1Effect1.setEffect(carielRoameAbility1Effect1Update)
    
################
# Add & Assign #
################
desc1 = lambda merc: 'Attack an enemy. *Deathblow*: Restore 40 health to %s' %('this merc.' if merc.equipmentName.lower() != 'hammer of dawn' else 'your characters.')
carielRoameAbility1.setDesc(desc1)
carielRoameAbility1.addEffect(carielRoameAbility1Effect1)
carielRoame.assignAbility(carielRoameAbility1)


##################
#                #
# Second Ability #
#                #
##################

carielRoameAbility2 = Ability('Taunt', 2, 1)
carielRoameAbility2.setDamage()

################
# First Effect #
################
carielRoameAbility2Effect1 = Effect('heal')
def carielRoameAbility2Effect1Update(board, actor, target=None):
    board.heal(actor.ID, 12)
carielRoameAbility2Effect1.addEffect(carielRoameAbility2Effect1Update)
    
################
# Second Effect #
################
carielRoameAbility2Effect2 = Effect('buff')
def carielRoameAbility2Effect2Update(board, actor, target=None):
    actor.taunt, actor.tauntCounter = True, 3
carielRoameAbility2Effect2.addEffect(carielRoameAbility2Effect2Update)

################
# Add & Assign #
################
desc2 = 'Restore 12 Health to this merc and gain Taunt for 3 turns.'
carielRoameAbility2.setDesc(desc2)
carielRoameAbility2.addEffect(carielRoameAbility2Effect1)
carielRoameAbility2.addEffect(carielRoameAbility2Effect2)
carielRoame.assignAbility(carielRoameAbility2)



#################
#               #
# Third Ability #
#               #
#################

carielRoameAbility3 = Ability('Seal of Light', 3, 4, 1)
carielRoameAbility3.setDamage()

################
# First Effect #
################
carielRoameAbility3Effect1 = Effect('heal')
def carielRoameAbility3Effect1Update(board, actor, target=None):
    board.heal(actor.ID, 15, target.ID)
carielRoameAbility3Effect1.addEffect(carielRoameAbility3Effect1Update)
    
################
# Second Effect #
################
carielRoameAbility3Effect2 = Effect('buff')
def carielRoameAbility3Effect2Update(board, actor, target=None):
    atk = 6 + 4*(actor.equipmentName.lower()=='tome of judgement')
    board.buff(actor.ID, atk=atk, buffeeID=target.ID)
carielRoameAbility3Effect2.addEffect(carielRoameAbility3Effect2Update)

################
# Add & Assign #
################
desc3 = lambda merc: 'Choose a character. Give it +%i Attack and restore 15 Health' %(6 if merc.equipmentName.lower() != 'tome of judgement' else 10)
carielRoameAbility3.setDesc(desc3)
carielRoameAbility3.addEffect(carielRoameAbility3Effect1)
carielRoameAbility3.addEffect(carielRoameAbility3Effect2)
carielRoame.assignAbility(carielRoameAbility3)