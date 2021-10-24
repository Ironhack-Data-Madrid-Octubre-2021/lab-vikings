
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health=health
        self.strength=strength   
    def attack(self):
        return self.strength
    def receiveDamage(self,amount):
        self.health=self.health - amount
# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        super().__init__(health,strength)
        self.name = name
    def receiveDamage(self, amount):
        self.health=self.health - amount
        if self.health>0:
            return f"{self.name} has received {amount} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return f"Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)
    def receiveDamage(self, amount):
        self.health=self.health - amount
        if self.health>0:
            return f"A Saxon has received {amount} points of damage"
        else:
            return f"A Saxon has died in combat"

# War

import random

class War():
    def __init__(self):
        vikingArmy:[]
        saxonArmy:[]
def addViking (self,viking):
    self.viking=viking
    self.vikingArmy.append(self.Viking)
def addSaxon(self,saxon):
    self.saxon=saxon
    self.saxonArmy.append(self.Saxon)
def vikingAttack(self):
    v1=random.choice(self.saxonArmy)
    v2=random.choice(self.vikingArmy)
    v3=v1.receiveDamage(v2.attack())
    for i in self.saxonArmy:
        if i.health <=0:
            self.saxonArmy.remove(i)
    return v3
def saxonAttack(self):
    s1=random.choice(self.vikingArmy)
    s2=random.choice(self.saxonArmy)
    s3=s1.receiveDamage(s2.attack())
    for i in self.vikingArmy:
        if i.health <= 0:
            self.vikingArmy.remove(i)
        return s3
def showStatus(self):
    if len(self.saxonArmy)==0:
        return "Vikings have won the war of the century!"
    if len(self.vikingArmy)==0:
        return "Saxons have fought for their lives and survive another day..."
    else:
        return "Vikings and Saxons are still in the thick of battle"