
# Soldier
class Soldier:
    """
    Soldiers class deliver fresh meat to the battlefield, just honorable people with two possibilities kill or die.
    They have health, and strength. Health is literally the points of live 
    and it will get reduce by de damage received. 
    Strength is the damage they can deliver to others when they attack.
    They are all equals.
    """

    # Constructor of class
    def __init__(self, health, strength):
        self.health = health 
        self.strength = strength
    
    # Methot to export damage to others
    def attack(self):
        return self.strength
    # Methot to reduce instance 

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking
class Viking(Soldier):
    """
    The lord of war of Vikings makes the born Soldiers to the shape of his realm. 
    Hi gives then a proper name, important because their creed, honor their names in combat, their names are the 
    wind that push their boats to the Valhalla when the fall in the battle.
    Every viking has a battle Cry
    """

    # Contructor of vikings
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    # Reinplement the methot to include lore extras
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f'{self.name} has died in act of combat'
        else:
            return f'{self.name} has received {damage} points of damage'
    
    # Methot to battle cry
    def battleCry(self):
        return 'Odin Owns You All!'


# Saxon
class Saxon(Soldier):
    """
    The King of all Saxons claim to his vassals for soldieres. Fresh meat and bone to hit and absorbe the inpacts. 
    No matters him who is behind the shield, if his saxon fall he give it to another one.
    """
    # Constructor of Saxons 
    def __init__(self, health, strength): 
        super().__init__(health, strength)
    
    # Reinplement the methot receiveDamge
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f'A Saxon has died in combat'
        else:
            return f'A Saxon has received {damage} points of damage'


# War

import random
class War:
    """.
    The G00D stuff: WAR. The Lord of War of Viking and the King of Saxons have a meeting.
    The call theirs armys....
    """
    # Constructor of the War
    # The 'self.**' under __init__ are variables of class
    # The 'self.**' under method are methods to aply to class vaiables, only self.
    #
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    # Method to add vikings to the empty array
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    
    # Method to add saxon to the empty array 
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    # Method to viking atack
    def vikingAttack(self):
        #(random.choice(self.saxonArmy)).receiveDamage((random.choice(self.vikingArmy)).strength)
        sajon = random.choice(self.saxonArmy)
        vikin = random.choice(self.vikingArmy)
        golpe = sajon.receiveDamage(vikin.attack())
        if sajon.health <= 0:
            self.saxonArmy.remove(sajon)
        return golpe

    # Method to Saxon atack
    def saxonAttack(self):
        #(random.choice(self.vikingArmy)).receiveDamage((random.choice(self.saxonArmy)).strength)
        sajon1 = random.choice(self.saxonArmy)
        vikin1 = random.choice(self.vikingArmy)
        golpe1 = vikin1.receiveDamage(sajon1.attack())
        if vikin1.health <= 0:
            self.vikingArmy.remove(vikin1)
        return golpe1
    
    # Method to check the status of the armys, this is how the game reache the end of itself.
    def showStatus(self):
        if len(self.saxonArmy)==0: 
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else: 
            return 'Vikings and Saxons are still in the thick of battle.' 











'''
#class War:
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        sax = random.choice(self.saxonArmy)
        vik = random.choice(self.vikingArmy)
        rec = sax.receiveDamage(vik.attack())

        if sax.health <= 0:
            self.saxonArmy.remove(sax)

        return rec

    def saxonAttack(self):
        sax1 = random.choice(self.saxonArmy)
        vik1 = random.choice(self.vikingArmy)
        rec1 = vik1.receiveDamage(sax1.attack())
        
        if vik1.health <= 0:
            self.vikingArmy.remove(vik1)

        return rec1

    def showStatus(self):
        if len(self.saxonArmy) == 0 :
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."

'''

