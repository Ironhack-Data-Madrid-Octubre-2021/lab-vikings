import random
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):

        self.health -= damage
        

# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.health = health
        self.strength = strength
        self.name = name

    def receiveDamage(self, damage):

        self.health -= damage 
        
        if self.health >0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        return 'Odin Owns You All!'
    
# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health >0 :
            return f'A Saxon has received {damage} points of damage'
        elif self.health <= 0:
            return f'A Saxon has died in combat'
   
        

# War


class War():
    def __init__(self):
        self.vikinarmy = []
        self.saxonarmy = []
    def addViking(self, viking):
        self.vikinarmy.append(viking)
        
    def addSaxon(self,saxon):
        self.saxonarmy.append(saxon)
        
    def vikingAttack(self):
        x = random.choice(self.saxonarmy)
        y = random.choice(self.vikinarmy)
        z = x.receiveDamage(y.attack) 
        if x.vida <=0:
            self.saxonarmy.remove(x)
        return z
    def saxonAttack(self):
        t = random.choice(self.saxonarmy)
        h = random.choice(self.vikinarmy)
        j = h.receiveDamage(t.attack)
        if h.vida <=0:
            self._vikinarmy.remove(h)
    def showStatus(self):
        if self._saxonarmy == False:
            print('Vikings have won the war of the century!')
        elif self._vikinarmy == False:
            print('Saxons have fought for their lives and survive another day...')
        elif len(self._vikinarmy) == 1 and len(self._saxonarmy) == 1:
            print('Vikings and Saxons are still in the thick of battle.')
