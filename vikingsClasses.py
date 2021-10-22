
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    def attack(self):
        return(self.strength)
        
    def receiveDamage(self,damage):
        self.health-=damage
    

# Viking
class Viking(Soldier):

    def __init__(self,name,health,strength):
        super().__init__(health,strength) 
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name}has died in act of combat"

    def battleCry(self):
        return ("Odin Owns You All!")

#Saxon

class Saxon(Soldier):

    def __init__(self,health,strength):
        super().__init__(health,strength) 
    
    def attack(self):
        return(self.strength)

    def receiveDamage(self,damage):
        self.health-=damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

#Wars

import random

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,oneviking):
        vikingArmy.append(oneviking):

    def addSaxon(self,onesaxon):
        saxonArmy.append(onesaxon):
    
    def vikingAttack(self):
        saxondeataque=random.choice(saxonArmy)
        vikingdeataque = random.choice(vikingArmy)
        saxondeataque.receiveDamage(vikingdeataque.strength)
        retorno = saxondeataque.receiveDamage(vikingdeataque.strength)

        if saxondeataque.strength =< 0:
            saxonArmy.remove(saxondeataque)
        
        return retorno 

    def saxonAttack(self):
        saxondeataque=random.choice(saxonArmy)
        vikingdeataque = random.choice(vikingArmy)
        vikingdeataque.receiveDamage(saxondeataque.strength)
        retorno = vikingdeataque.receiveDamage(saxondeataque.strength)

        if vikingdeataque.strength =< 0:
            vikingArmy.remove(vikingdeataque)
        
        return retorno     

    def showStatus(self):
        if self.saxonArmy is 0:
            return "Vikings have won the war of the century!"
        if self.vikingArmy is 0:
            return "Saxons have fought for their lives and survive another day..."
        if self.saxonArmy=<1 and self.vikingArmy<1:
            return "Vikings and Saxons are still in the thick of battle."

