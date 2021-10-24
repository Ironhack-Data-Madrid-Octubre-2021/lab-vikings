import random

# Soldier
class Soldier:

    def __innit__(self, health, strength):
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
    
    def attack(self):
        super().attack()
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    
    def battleCry():
        return 'Odin Owns You All!'


# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack(self):
        super().attack()
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return 'A Saxon has died in combat'


# War
class War:

    def __init__(self):
        self.saxonArmy = []
        self.vikingArmy = []
    
    def addViking(self, viking):
        self.viking = viking
        self.vikingArmy.append(self.viking)

    def addSaxon(self, saxon):
        self.saxon = saxon
        self.saxonArmy.append(self, saxon)

    def vikingAttack(self):
        sa = random.choice(self.saxonArmy)
        va = random.choice(self.vikingArmy)
        rd = sa.receiveDamage(va.attack())

        for i in self.saxonArmy:
            if i.health <= 0:
                self.saxonArmy.remove(i)
        return rd

    def saxonAttack(self):
        va = random.choice(self, vikingArmy)
        sa = random.choice(self.saxonArmy)
        rd = va.receiveDamage(sa.attack())

        for i in self.vikingArmy:
            if i.health <= 0:
                self.vikingArmy.remove(i)
        return rd

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century'
        if len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'
        

        

    
