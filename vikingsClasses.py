import random
# Soldier --> OK
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength 

    def receiveDamage(self,damage):
        self.health -= damage

# Viking --> OK
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
            return f"{self.name} has received {damage} points of damage"
        if self.health <= 0:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!" 

# Saxon --> OK
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        super().attack()
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        if self.health <= 0:
            return f"A Saxon has died in combat"

# War
class War: #OK
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking): #OK
        self.viking=viking
        self.vikingArmy.append(self.viking)

    def addSaxon(self, saxon): #OK
        self.saxon=saxon
        self.saxonArmy.append(self.saxon)

    def vikingAttack(self):
        a = random.choice(self.saxonArmy) #self.saxon desde self.saxonArmy
        b = random.choice(self.vikingArmy) #self.viking desde self.vikingArmy
        z = a.receiveDamage(b.attack()) #coge al sajón elegido, le aplica su alg de daño -que funciona con damage, que es = fuerza, que se recupera con attack().

        for i in self.saxonArmy:
            if i.health <= 0:
                self.saxonArmy.remove(i)
        return z

    def saxonAttack(self):
        a = random.choice(self.vikingArmy)
        b = random.choice(self.saxonArmy)
        z = a.receiveDamage(b.attack())

        for i in self.vikingArmy:
            if i.health <= 0:
                self.vikingArmy.remove(i)
        return z

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."