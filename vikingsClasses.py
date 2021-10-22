
# Soldier
class Soldier:
    def __init__(self,health,strength) :
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0 :
            return f"{self.name} has received {damage} points of damage"
        else :
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0 :
            return f"A Saxon has received {damage} points of damage"
        else :
            return f"A Saxon has died in combat"

import random
# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,v) :
        self.vikingArmy.append(v)        

    def addSaxon(self,s) :
        self.saxonArmy.append(s)

    def vikingAttack(self) :
        defensor = random.choice(self.saxonArmy)
        atacante = random.choice(self.vikingArmy)
        mensaje = defensor.receiveDamage(atacante.strength)
        if defensor.health <= 0 :
            self.saxonArmy.remove(defensor)
        return mensaje

    def saxonAttack(self) :
        defensor = random.choice(self.vikingArmy)
        atacante = random.choice(self.saxonArmy)
        mensaje = defensor.receiveDamage(atacante.strength)
        if defensor.health <= 0 :
            self.vikingArmy.remove(defensor)
        return mensaje

    def showStatus(self) :
        if len(self.saxonArmy) == 0 :
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0 :
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.vikingArmy) >= 1  and len(self.saxonArmy) >= 1 :
            return "Vikings and Saxons are still in the thick of battle."
        
    
