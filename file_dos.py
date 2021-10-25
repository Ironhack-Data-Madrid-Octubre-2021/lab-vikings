#import classes from vikingsClasses.py

# Soldier
class Soldier:
    def __init__(self, health, strength):
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

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"
    
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
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
        sax = random.choice(self.saxonArmy)
        vik = random.choice(self.vikingArmy)
       
        rec = sax.receiveDamage(vik.attack())
    
        if sax.health <= 0:
            self.saxonArmy.remove(sax)

        return rec

    def saxonAttack(self):
        sax = random.choice(self.saxonArmy)
        vik = random.choice(self.vikingArmy)
        
        rec = vik.receiveDamage(sax.attack())

        if vik.health <= 0:
            self.vikingArmy.remove(vik)
        
        return rec

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."


#create objets of the class Viking
viking_names = ["Ragnar","Rolo","Floki","Bjorn","Lagertha","Ubbe","Porunn", "Torvi", "Helga", "Siggy"]
#saxon_names  = ["Aiken","Bardon","Eamon","Athelstan","Egbert","Aelle","Aethelwulf","Morton","Svein","Wystan"]

vik1 = Viking("",0,0)
vik2 = Viking("",0,0)
vik3 = Viking("",0,0)
vik4 = Viking("",0,0)
vik5 = Viking("",0,0)
vik6 = Viking("",0,0)
vik7 = Viking("",0,0)
vik8 = Viking("",0,0)
vik9 = Viking("",0,0)
vik0 = Viking("",0,0)

viks = [vik1,vik2,vik3,vik4,vik5,vik6,vik7,vik8,vik9,vik0]

i = 0
for vik in viks: #asignar la vida y el poder de forma random a los objetos de la clase
    vik.name = viking_names[i]
    vik.health = random.randrange(80,101)
    vik.strength = random.randrange(25,36)
    i+= 1

#create objets of the Class Saxon;
sax1 = Saxon(0,0)
sax2 = Saxon(0,0)
sax3 = Saxon(0,0)
sax4 = Saxon(0,0)
sax5 = Saxon(0,0)
sax6 = Saxon(0,0)
sax7 = Saxon(0,0)
sax8 = Saxon(0,0)
sax9 = Saxon(0,0)
sax0 = Saxon(0,0)

saxs = [sax1,sax2,sax3,sax4,sax5,sax6,sax7,sax8,sax9,sax0]

i = 0
for sax in saxs:
    sax.health = random.randrange(80,101)
    sax.strength = random.randrange(25,36)
    i+= 1


#create 1 class of the Class War that has a different result each time is run:
import time
war2 = War()

for v in viks:
    war2.addViking(v)
for s in saxs:
    war2.addSaxon(s)


usu = input("Elige ejercito: V para Vikingos y S para Sajones: ")

if usu.lower() == v:

    while (len(war2.vikingArmy) > 0) and (len(war2.saxonArmy) >0):



            
        print(f"vikings attack:\n{vik.name} yells: {vik.battleCry()}")
        print(war2.vikingAttack()) #en un archivo python cada vez que haces print ejectua la sentencia que printeas ¡¡Recuerda!!
        print(f"{war2.showStatus()}\n")
        time.sleep(1)
        if (len(war2.vikingArmy) == 0) or (len(war2.saxonArmy) == 0):
            break
        
        
        print(f"saxons attack: ")
        print(war2.saxonAttack())
        print(f"{war2.showStatus()}\n")
        time.sleep(1)
        

        if (len(war2.vikingArmy) == 0) or (len(war2.saxonArmy) == 0):
            break
    
else:
    while (len(war2.vikingArmy) > 0) and (len(war2.saxonArmy) >0):
        print(f"saxons attack: ")
        print(war2.saxonAttack())
        print(f"{war2.showStatus()}\n")
        time.sleep(1)
        if (len(war2.vikingArmy) == 0) or (len(war2.saxonArmy) == 0):
            break
        

        print(f"vikings attack:\n{vik.name} yells: {vik.battleCry()}")
        print(war2.vikingAttack()) #en un archivo python cada vez que haces print ejectua la sentencia que printeas ¡¡Recuerda!!
        print(f"{war2.showStatus()}\n")
        time.sleep(1)

        if (len(war2.vikingArmy) == 0) or (len(war2.saxonArmy) == 0):
            break
        