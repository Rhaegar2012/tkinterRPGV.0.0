# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:20:18 2019

@author: joseb
"""
import random 
#Base character class
class Character():
    def __init__(self):
        self.strenght=0
        self.agility=0
        self.stamina=0
        self.constitution=0
        self.influence=0
        self.intelligence=0
        self.wisdom=0
        self.health=0
    def attack(self):
        hit= False
        roll=random.randint(0,20)
        if self.agility>=5 and roll>=12:
            hit=True
        elif self.agility>=10 and roll>=8:
            hit=True
        elif self.agility>=12 and roll>=5:
            hit=True
        if hit is True:
            damage=random.uniform(self.strength*0.35,self.strength*0.75)
        else:
            damage=0

        return int(damage)
    def defend(self,base_damage):
        roll=random.randint(0,20)
        if self.constitution>=5 and roll>=10:
            base_damage=base_damage*0.90
        elif self.constitution>=10 and roll>=8:
            base_damage=base_damage*0.80
        elif self.constitution>=12 and roll>=5:
            base_damage=base_damage*0.75
        self.health=self.health-int(base_damage)
        if self.health<0:
            self.health=0
        return self.health
    
    def use_item(self):
        pass
#Combat Operative Character class
class Combat_Operative(Character):
    def __init__(self,strength=10,agility=10,stamina=8,influence=4,intelligence=6,wisdom=7,health=11,constitution=10):
        self.strength=strength 
        self.agility=agility
        self.stamina=stamina
        self.influence=influence
        self.intelligence=intelligence
        self.wisdom=wisdom
        self.health=health
        self.constitution=constitution
#Tech Operative Character class
class Tech_Operative(Character):
    def __init__(self,strength=7,agility=7,stamina=5,influence=7,intelligence=10,wisdom=8,health=8,constitution=6):
        self.strength=strength
        self.agility=agility
        self.stamina=stamina
        self.influence=influence
        self.intelligence=intelligence
        self.wisdom=wisdom
        self.health=health
        self.constitution=constitution
#Covert Operative Character class
class Covert_Operative(Character):
    def __init__(self,strength=6,agility=9,stamina=6,influence=10,intelligence=8,wisdom=11,health=8,constitution=8):
        self.strength=strength
        self.agility=agility
        self.stamina=stamina
        self.influence=influence
        self.intelligence=intelligence
        self.wisdom=wisdom
        self.health=health
        self.constitution=constitution
        
#Enemy Class
class Enemy(Character):
    def __init__(self,strenght=8,agility=7,constitution=10,health=15,stamina=9):
        self.strength=strenght
        self.agility=agility
        self.constitution=constitution
        self.health=health
        self.stamina=stamina
#Main Game Loop
        

        
    
    
    
        
    