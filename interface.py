# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 14:57:44 2019

@author: joseb
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
import character
win=tk.Tk()
win.title("V1.0")
#Enemy and Character Objects
enemy=character.Enemy()
player=character.Combat_Operative()
#button actions
def attack_press():
    enemy_init_health=enemy.health
    damage = player.attack()
    enemy_health=enemy.defend(damage)
    absorbed_damage=(damage-(enemy_init_health-enemy_health))
    Action_button=ttk.Button(player_control,text="Action",command=command_action)
    Action_button.grid(column=0,row=0)
    Action_button.configure(state="disabled")
    Flee_button=ttk.Button(player_control,text="Flee")
    Flee_button.grid(column=0,row=1)
    Flee_button.configure(state="disabled")
    Guard_button=ttk.Button(player_control,text="Guard")
    Guard_button.grid(column=1,row=0)
    Guard_button.configure(state="disabled")
    Pass_button=ttk.Button(player_control,text="Pass",command=enemy_attack)
    Pass_button.grid(column=1,row=1,sticky=tk.W)
    player_message=ttk.Label(action_console,text="Player Attacks! deals %s damage"%damage)
    player_message.grid(row=0,column=0)
    enemy_hp=ttk.Label(enemy_stats,text="Hp: %s"%enemy_health)
    enemy_hp.grid(row=0,column=0)
    enemy_message=ttk.Label(enemy_console,text="Enemy absorbs %s  damage"%absorbed_damage)
    enemy_message.grid(column=0,row=1)
    if enemy.health==0:
        mBox.showinfo("Python Message Info Box","You´ve won, restart the simulator!!!")

def enemy_attack():
    player_init_health=player.health
    damage=enemy.attack()
    player_health=player.defend(damage)
    absorbed_damage=damage-(player_init_health-player_health)
    player_hp=ttk.Label(player_stats,text="Hp: %s"%player_health)
    player_hp.grid(row=0,column=0)
    Action_button=ttk.Button(player_control,text="Action",command=command_action)
    Action_button.grid(column=0,row=0)
    Flee_button=ttk.Button(player_control,text="Flee")
    Flee_button.grid(column=0,row=1)
    Guard_button=ttk.Button(player_control,text="Guard")
    Guard_button.grid(column=1,row=0)
    Pass_button=ttk.Button(player_control,text="Pass",command=enemy_attack)
    Pass_button.grid(column=1,row=1)
    Pass_button.configure(state="disabled")
    Pass_button.grid(column=1,row=1,sticky=tk.W)
    enemy_message=ttk.Label(enemy_console,text="Enemy Attacks! deals %s damage"%damage)
    enemy_message.grid(row=1,column=0)
    player_message=ttk.Label(action_console,text="Player absorbs %s damage"%absorbed_damage)
    player_message.grid(row=0,column=0)
    if player.health==0:
        mBox.showinfo("Python Message Info Box", "You lose , try again!")
    
    

def command_action():
    Action_button.destroy()
    Flee_button.destroy()
    Guard_button.destroy()
    Pass_button.destroy()
    Attack_button=ttk.Button(player_control,text="Attack",command=attack_press)
    Attack_button.grid(column=0,row=0)
    Use_button=ttk.Button(player_control,text="Use Item")
    Use_button.grid(column=1,row=0)
    Hability_button=ttk.Button(player_control,text="Habilities")
    Hability_button.grid(column=0,row=1)


   
    
    
    
#Action buttons
#Creates a label for the player screen 
screen=ttk.LabelFrame(win,text="Main Screen")
screen.grid(column=0,row=0)
#Creates a label for the player control
player_control=ttk.LabelFrame(win,text="Player Options")
player_control.grid(column=0,row=2,sticky=tk.W)
#Creates a label frame for the Enemy
enemy_console=ttk.LabelFrame(win, text="Enemy Console")
enemy_console.grid(column=0,row=2)
#Add player buttons 
Action_button=ttk.Button(player_control,text="Action",command=command_action)
Action_button.grid(column=0,row=0)
Flee_button=ttk.Button(player_control,text="Flee")
Flee_button.grid(column=0,row=1)
Guard_button=ttk.Button(player_control,text="Guard")
Guard_button.grid(column=2,row=0)
Pass_button=ttk.Button(player_control,text="Pass",command=enemy_attack)
Pass_button.grid(column=2,row=1)
Pass_button.configure(state="disabled")
#Adds Enemy Console 
console=ttk.Label(enemy_console,text="Enemy Standby")
console.grid(column=0,row=1)
canvas=tk.Canvas(screen,bg="white",height=400,width=2000)
#Add Player Action Console
console=ttk.LabelFrame(win,text="Player Actions")
console.grid(column=0,row=3)
action_console=ttk.Label(console,text="Player Standby")
action_console.grid(column=0,row=0)
#Draws player and enemy stat bars 
player_stats=ttk.LabelFrame(win,text="Player Stats")
player_stats.grid(row=1,column=0,sticky=tk.W)
player_hp=ttk.Label(player_stats,text="HP: %s"%player.health)
player_hp.grid(row=0,column=0)
player_stamina=ttk.Label(player_stats,text="Stamina: %s"%player.stamina)
player_stamina.grid(row=1,column=0)
enemy_stats=ttk.LabelFrame(win,text="Enemy Stats")
enemy_stats.grid(row=1,column=0)
enemy_hp=ttk.Label(enemy_stats,text="HP: %s"%enemy.health)
enemy_hp.grid(column=0,row=0)
enemy_stamina=ttk.Label(enemy_stats,text="Stamina: %s"%enemy.stamina)
enemy_stamina.grid(column=0,row=1)
#Draws player circle
x1=100
y1=30
x0=300
y0=230
player_circle=canvas.create_oval(x0,y0,x1,y1,fill="blue")
player_label=canvas.create_text((200,300), text="Player",font=20)
#Draw Enemy Rectangle 
x1=1100
y1=30
x0=1300
y0=230
enemy_rectangle=canvas.create_rectangle(x0,y0,x1,y1,fill="red")
enemy_label=canvas.create_text((1200,300),text="Enemy",font=20)
canvas.pack()

#Reset State  

if player.health==0:
    mBox.showinfo("Python Message Info Box", "You lose , try again!")
elif enemy.health==0:
    mBox.showinfo("Python Message Info Box","You´ve won, restart the simulator!!!")
    
    


win.mainloop()