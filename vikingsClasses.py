
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
        unsaxoncualquiera = random.choice(self.saxongArmy)

        retorno = unsaxoncualquiera.receiveDamage(unvikingcualquiera.strength)

        if unsaxoncualquiera.strength <= 0:
            saxonArmy.remove(unsaxoncualquiera)
        
        return retorno

    





        


        

#class War:
 
