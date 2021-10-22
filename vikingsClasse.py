import random
# Soldier

class Soldier:
    def __init__(self,health, strength):
        self._vida = health
        self._fuerza = strength
    def attack(self):
        return self._fuerza
    def receiveDamage(self, damage):
        self._vida -damage
        

# Viking


class Viking(Soldier):
    def __init__(self, name, vida,fuerza):
        super().__init__(vida, fuerza)
        self._nombre = name
    def receiveDamage(self, damage):
        self._vida -damage 
        if self._vida >0 :
            print(f'{self._nombre} has received {damage} points of damage. ')
        elif self._vida <=0:
            print(f'{self._nombre} has died in act of combat. ')
    def battleCry():
        return 'Odin Owns You All!'
    
# Saxon


class Saxon(Soldier):
    def __init__(self, vida, fuerza):
        super().__init__(vida, fuerza)
    def receiveDamage(self, damage):
        if self._vida >0 :
            print(f'A Saxon has received {damage} points of damage. ')
        elif self._vida <=0:
            print(f'A Saxon has died in act of combat. ')
   
        

# War


class War():
    def __init__(self,viking = [], saxon= []):
        self._vikinarmy = viking
        self._saxonarmy = saxon
    def addViking(self, viking):
        self._vikinarmy.append(viking)
        self._vikinarmy.append(viking)
        self._vikinarmy.append(viking)
        self._vikinarmy.append(viking)
        self._vikinarmy.append(viking)
        self._vikinarmy.append(viking)
        self._vikinarmy.append(viking)
        self._vikinarmy.append(viking)
        self._vikinarmy.append(viking)
        self._vikinarmy.append(viking)
    def addSaxon(self,saxon):
        self._saxonarmy.append(saxon)
        self._saxonarmy.append(saxon)
        self._saxonarmy.append(saxon)
        self._saxonarmy.append(saxon)
        self._saxonarmy.append(saxon)
        self._saxonarmy.append(saxon)
        self._saxonarmy.append(saxon)
        self._saxonarmy.append(saxon)
        self._saxonarmy.append(saxon)
        self._saxonarmy.append(saxon)
    def vikingAttack(self):
        x = random.choice(self._saxonarmy)
        y = random.choice(self._vikinarmy)
        z = x.receiveDamge(y.attack) 
        if x.vida <=0:
            self._saxonarmy.remove(x)
        return z
    def saxonAttack(self):
        t = random.choice(self._saxonarmy)
        h = random.choice(self._vikinarmy)
        j = h.receiveDamge(t.attack)
        if h.vida <=0:
            self._vikinarmy.remove(h)
    def showStatus(self):
        if self._saxonarmy == False:
            print('Vikings have won the war of the century!')
        elif self._vikinarmy == False:
            print('Saxons have fought for their lives and survive another day...')
        elif len(self._vikinarmy) == 1 and len(self._saxonarmy) == 1:
            print('Vikings and Saxons are still in the thick of battle.')