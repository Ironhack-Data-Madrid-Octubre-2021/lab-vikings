
# Soldier


class Soldier():
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage
        

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"



# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# War

import random

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,oneviking):
        self.vikingArmy.append(oneviking)

    def addSaxon(self,onesaxon):
        self.saxonArmy.append(onesaxon)

    def vikingAttack(self):
        unvikingcualquiera = random.choice(self.vikingArmy)
        unsaxoncualquiera = random.choice(self.saxonArmy)

        retorno = unsaxoncualquiera.receiveDamage(unvikingcualquiera.strength)

        if unsaxoncualquiera.strength <= 0:
            saxonArmy.remove(unsaxoncualquiera)
        
        return retorno
    
    def saxonAttack(self):
        unvikingcualquiera = random.choice(self.vikingArmy)
        unsaxoncualquiera = random.choice(self.saxonArmy)

        retorno1 = unvikingcualquiera.receiveDamage(unsaxoncualquiera.strength)

        if unvikingcualquiera.strength <= 0:
            saxonArmy.remove(unvikingcualquiera)
        
        return retorno1

    def showStatus(self):

        if len(self.saxonArmy) == 0:
            return'Vikings have won the war of the century!'

        elif len(self.vikingArmy) == 0:
            return'Saxons have fought for their lives and survive another day...'
        
        else:
            return"Vikings and Saxons are still in the thick of battle."
        
