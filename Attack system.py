import random
peter_DP_list=[3,4,5,6,]
peter_HP=20
peter_armor_HP=1
mangos_HP=10

def peter_normal_damage() :
            peter_DP=random.choice(peter_DP_list) #give a random attack value of Peter

def peter_normal_turn():
        global mangos_armor_hp,mangos_HP
        peter_damage = peterNormalDamage()
        peter_DP= peter_damage - mangos_armor_HP
        mangos_HP= mangos_HP - damage
        print("you inflicted",peter_DP,"damage to the mongose !")
        print("the mangos still have",mangos_HP,"HP")
        return
            
def special_attack(b):
    while b!=0 and b!=1 and b!=2 and b!=3:
        print("Invalid choice. Please enter a valid option.")
        a=int(input("Choose your special attack: \n Defend: enter 1 \n Snake eyes: enter 2 \n Last chance: enter 3 \n If you want to go back to regular attack: enter 0\n"))
    if b==1: #Defend: armorPV *2 + regular attack
        peter_armor_HP = peter_armor_HP*2
        if peter_HP%2==0:
            peter_normal_turn()
        print("Peter's armor is now", peter_armor_HP, "\n")
    if b==2: #Snake eyes: regular attack + DP inflicted = DP gained => fonction 'bin'
        snake_eyes()
    if b==3: #Last chance: DP max *3 but sometimes miss the target
        mangos_hp = mangos_hp-(peter_DP_list[3]*3) #hits for maximum damage multiplied by 3
        
        print("Executing a special attack, Peter inflicted", peter_DP, "\n")

a=int(input("Oh no! A mangoose is coming.\nStart of the fight, choose your attack:\nNormal attack: enter 0\nSpecial attack: enter another value\n"))
def attack(a):
    if a==0: #Tristan
        peter_normal_turn()
    else:
        b=int(input("Choose your special attack: \n Defend: enter 1 \n Snake eyes: enter 2 \n Last chance: enter 3 \n If you want to go back to regular attack: enter 0\n")      
        special_attack(b)
attack(a)

                        #random.choice
#def random_attack():

