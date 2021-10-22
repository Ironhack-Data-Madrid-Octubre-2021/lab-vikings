
# Soldier
class Soldier:
    def __init__(self, health, strength):
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
            return f"A Saxon has died in combat"


# War

import random
class War:
     
    def __init__(self):
        self.vikingArmy = [] 
        self.saxonArmy = []
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        sax = random.choice(self.saxonArmy)
        vik = random.choice(self.vikingArmy)
       
        rec = sax.receiveDamage(vik.attack())
    
        if sax.health <= 0:
            self.saxonArmy.remove(sax)

        return rec

    def saxonAttack(self):
        sax1 = random.choice(self.saxonArmy)
        vik1 = random.choice(self.vikingArmy)
        
        rec1 = vik1.receiveDamage(sax1.attack())

        if vik1.health <= 0:
            self.vikingArmy.remove(vik1)
        
        return rec1

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."