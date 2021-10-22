
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    

    def attack(self):
        return self.strength
        

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name = name


    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


    def battleCry(self):
        return "Odin Owns You All!"




# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)


    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
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

    
    def addViking(self, viking):
        self.vikingArmy.append(viking)

    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damageSaxon = saxon.receiveDamage(viking.attack())
        if saxon.health<=0:
            self.saxonArmy.remove(saxon)
        return damageSaxon

    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damageViking = viking.receiveDamage(saxon.attack())
        if viking.health <=0:
            self.vikingArmy.remove(viking)
        return damageViking

    
    def showStatus(self):
        if len(self.saxonArmy) ==0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) ==0:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."


