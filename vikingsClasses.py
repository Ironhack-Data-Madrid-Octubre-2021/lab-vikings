
# Soldier

class Soldier:
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self,dam):
        self.health-=dam


# Viking

class Viking(Soldier):
    def __init__(self,name,health,strength):
        super().__init__(health,strength)
        self.name=name

    def receiveDamage(self,dam):
        self.health-=dam
        if self.health>0:
            return f"{self.name} has received {dam} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)

    def receiveDamage(self,dam):
        self.health-=dam
        if self.health>0:
            return f"A Saxon has received {dam} points of damage"
        else:
            return "A Saxon has died in act of combat"


# War

import random

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self,v):
        self.vikingArmy.append(v)

    def addSaxon(self,s):
        self.saxonArmy.append(s)

    def vikingAttack(self):
        sax=random.choice(self.saxonArmy)
        vik=random.choice(self.vikingArmy)
        sax.receiveDamage(vik.attack())
        if sax.health<=0:
            self.saxonArmy.remove(sax)

    def saxonAttack(self):
        sax=random.choice(self.saxonArmy)
        vik=random.choice(self.vikingArmy)
        vik.receiveDamage(sax.attack())
        if vik.health<=0:
            self.vikingArmy.remove(vik)

    def showStatus(self):
        if self.vikingArmy==[]:
            return "Saxons have fought for their lives and survive another day..."
        elif self.saxonArmy==[]:
            return "Vikings have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."
