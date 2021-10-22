
# Soldier
import random

class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health -= damage
    

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.health = health
        self.strength = strength
        self.name = name
    
    def receiveDamage(self, damage):
        
        self.health -= damage

        if self.health > 0:
            
            return  f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    
    def battleCry(self):
        return 'Odin Owns You All!'

    

# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    
    def receiveDamage(self, damage):
        
        self.health -= damage

        if self.health > 0:
            
            return  f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'


# War


class War:

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self,viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        atacante = random.choice(self.vikingArmy)
        defensor = random.choice(self.saxonArmy)
        retorno = defensor.receiveDamage(atacante.strength)
        if defensor.health <= 0:
            self.saxonArmy.remove(defensor)
    
        return retorno

    def saxonAttack(self):
        defensor = random.choice(self.vikingArmy)
        atacante = random.choice(self.saxonArmy)
        retorno =  defensor.receiveDamage(atacante.strength)
        if defensor.health <= 0:
            self.vikingArmy.remove(defensor)
    
        return retorno

    def showStatus(self):

        if len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        elif len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'

