
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.damage = damage
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
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
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        SaxonDmg = random_saxon.receiveDamage(random_viking.attack())

        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        
        return SaxonDmg

    def saxonAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        VikingDmg = random_viking.receiveDamage(random_saxon.attack())

        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        
        return VikingDmg

    def showStatus(self):
        if len(self.saxonArmy) ==0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) ==0:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."







    
