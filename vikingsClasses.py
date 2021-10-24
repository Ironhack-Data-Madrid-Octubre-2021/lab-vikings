
# Soldier
import random

class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    def  __init__(self,name,health,strength):
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def  battleCry(self):
        return "Odin owns you ALL!"


# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
         self.health = health
         self.strength = strength
    
    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
    

# War


class War:
    def  __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self,viking):
        self.viking = viking
        self.vikingArmy.append(self.viking)

    def addSaxon(self,saxon):
        self.saxon = saxon
        self.saxonArmy.append(self.saxon)

    def vikingAttack(self):
        randomsaxon = random.choice (self.saxonArmy)
        randomviking = random.choice (self.vikingArmy)
        receiveviking = randomsaxon.receiveDamage(randomviking.attack())
        for i in self.saxonArmy:
            if i.health <= 0:
                self.saxonArmy.remove(i)
        return receiveviking
    
    def saxonAttack(self):
        randomviking = random.choice(self.vikingArmy)
        randomsaxon = random.choice(self.saxonArmy)
        receivesaxon = randomviking.receiveDamage(randomsaxon.attack())
        for i in self.vikingArmy:
            if i.health <= 0:
                self.vikingArmy.remove(i)
        return receivesaxon

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."