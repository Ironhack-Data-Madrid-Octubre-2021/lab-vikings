
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage=damage
        self.health=self.health-damage


# Viking


class Viking(Soldier):
    def __init__(self,name,health, strength):
        super().__init__(health,strength) 
        self.name=name

    def receiveDamage(self,damage):
        self.damage=damage
        self.health=self.health-damage
        if self.health>0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)
    
    def receiveDamage(self,damage):
        self.damage=damage
        self.health=self.health-damage
        if self.health>0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War

import random

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
        
    def vikingAttack(self):
        attack=random.choice(self.vikingArmy)
        deffend=random.choice(self.saxonArmy)
        herida=deffend.receiveDamage(attack.strength)
        if deffend.health<=0:
            self.saxonArmy.remove(deffend)
        return herida

    def saxonAttack(self):
        attack=random.choice(self.saxonArmy)
        deffend=random.choice(self.vikingArmy)
        herida=deffend.receiveDamage(attack.strength)
        if deffend.health<=0:
            self.vikingArmy.remove(deffend)
        return herida

    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else: 
            return "Vikings and Saxons are still in the thick of battle."