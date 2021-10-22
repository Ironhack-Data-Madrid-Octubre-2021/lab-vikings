
# Soldier

class Soldier:
    #constructor function:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    #método attack:
    def attack(self):
        return self.strength

    #método receiveDamage:
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage


# Viking

class Viking(Soldier):
    #constructor function
    def __init__(self,name, health, strenght):
        super().__init__(health, strenght)
        self.name = name

    #método attack:
    def attack(self):
        return self.strength 

    #método receiveDamage:
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    #método battleCry:
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    #constructor function
    def __init__(self,health, strength):
        super().__init__(health, strength)
    
    #método attack:
    def attack(self):
        return self.strength
    
    #método receiveDamage:
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


# War

import random
class War:


    #constructor function:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    #método `addViking()`
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
    
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)

    #`vikingAttack()` method
    def vikingAttack(self):
        unsaxoncualquiera = random.choice(self.saxonArmy)
        unvikingcualquiera = random.choice(self.vikingArmy)
        dmgSaxon = unsaxoncualquiera.receiveDamage(unvikingcualquiera.attack())
        
        if unsaxoncualquiera.health <= 0:
            self.saxonArmy.remove(unsaxoncualquiera)
        return dmgSaxon
        

    def saxonAttack(self):
        unsaxoncualquiera = random.choice(self.saxonArmy)
        unvikingcualquiera = random.choice(self.vikingArmy)
        dmgViking = unvikingcualquiera.receiveDamage(unsaxoncualquiera.attack())
        
        if unvikingcualquiera.health <= 0:
            self.vikingArmy.remove(unvikingcualquiera)
        return dmgViking
        

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) ==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."



