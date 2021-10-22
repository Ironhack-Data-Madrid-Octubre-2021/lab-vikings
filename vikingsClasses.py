
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.damage = damage
        self.health -= damage 



# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name = name
        super().__init__(health,strength)
        
    def attack(self):
        return super().attack()

    def receiveDamage(self,damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"



# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)

    def attack(self):
        return super().attack()

    def receiveDamage(self,damage):
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
        atacado = random.choice(self.saxonArmy)
        atacante = random.choice(self.vikingArmy)
        retorno = atacado.receiveDamage(atacante.strength)
        if atacado.health <= 0:
            self.saxonArmy.remove(atacado)
        return retorno

    def saxonAttack(self):
        atacado1 = random.choice(self.vikingArmy)
        atacante1 = random.choice(self.saxonArmy)
        retorno1 = atacado1.receiveDamage(atacante1.strength)
        if atacado1.health <= 0:
            self.vikingArmy.remove(atacado1)
        return retorno1

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) ==0:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."








        

