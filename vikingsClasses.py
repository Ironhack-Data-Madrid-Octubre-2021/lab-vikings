
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
        vikingArmy.append(oneviking)

    def addSaxon(self,onesaxon):
        saxonArmy.append(onesaxon)
    
    def vikingAttack():
        unsaxoncualquiera = random.choice(saxonArmy)
        unvikingcualquiera = random.choice(vikingArmy)
        
        retorno = unsaxoncualquiera.receiveDamage(unvikingcualquiera.strength)

        if unsaxoncualquiera.strength = < 0:
            saxonArmy.remove(unsaxoncualquiera)
        
        return retorno

    def saxonAttack():
        unvikingcualquiera = random.choice(vikingArmy)
        unsaxoncualquiera = random.choice(saxongArmy)
        
        retorno = unvikingcualquiera.receiveDamage(unsaxoncualquiera.strength)

        if unvikingcualquiera.strength =< 0:
            vikingArmy.remove(unvikingcualquiera)
        
        return retorno





        


        

#class War:
 
