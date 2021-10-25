
# Soldier


from _typeshed import Self


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage (self, damage):
        self.health = self.health - damage



# Viking

class Viking (Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry (self): 
        return "Odin Owns You All!"

    pass

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        viking_index = choice(range(len(self.vikingArmy)))
        saxon_index = choice(range(len(self.saxonArmy)))
        viking_attack = self.vikingArmy[viking_index].attack()
        receive_damage_result = self.saxonArmy[saxon_index].receiveDamage(viking_attack)
        ##                      Give me the saxon of the given index; .apply to him the receiveDamage method, where the damage is = to the attack of given viking 

        if self.saxonArmy[saxon_index].health <= 0:
            self.saxonArmy.pop(saxon_index)
        
        return receive_damage_result

    def saxonAttack(self):
        saxon_index = choice(range(len(self.saxonArmy)))
        viking_index  = choice(range(len(self.vikingArmy)))
        saxon_attack = self.saxonArmy[saxon_index].attack()
        
        receive_damage_result = self.vikingArmy[viking_index].receiveDamage(saxon_attack)

        if self.vikingArmy[viking_index].health <= 0:
            self.vikingArmy.pop(viking_index)
        return receive_damage_result



    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        
        return "Vikings and Saxons are still in the thick of battle."
