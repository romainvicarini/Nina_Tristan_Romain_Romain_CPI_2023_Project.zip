import random


def peter_normal_damage() :
    peter_DP=random.choice(peter_DP_list) #give a random attack value of Peter
    return peter_DP

def mangos_normal_damage():
    mangos_DP=random.choice(mangos_DP_list) #give a random attack value of mangos
    return mangos_DP

print("Oh no! A mangoose is coming.\nStart of the fight, choose your attack:\nNormal attack: enter True\nSpecial attack: enter False")
def attack(n):
    if n==True:
        #Tristan is loading... 
    if n==False:
        print("Choose your special attack: \n Defend: enter 1 \n Snake eyes: enter 2 \n Last chance: enter 3 \n If you want to go back to regular attack: enter True")
            def specialattack(n):
                if n==1: #defend = armorPV *2 + regular attack
                    peter_armor_HP = peter_armor_HP*2
                    if peter_HP%2==0:
                        peter_normal_damage()
                if n==2: snake eyes #regular attack + DP inflicted = DP gained => fonction 'bin'
                    #see regular attack
                    peter_HP = peter_HP + peter_DP
                if n==3: last chance #DP max *3 but sometimes miss the target
                        lastchance = False
                        mangos_hp = mangos_hp-???*3 #hits for maximum damage multiplied by 3
                        peter_normal_damage()


def peter_normal_turn():
        global mangos_armor_hp,mangos_HP
        peter_damage = peterNormalDamage()
        damage= peter_damage - mangos_armor_HP
        mangos_HP= mangos_HP - damage
        print("you inflicted",damage,"damage to the mongose !")
        print("the mangos still have",mangos_HP,"HP")
        return

def snakeEyes():
    global mangos_HP, Peter_HP
    a=0
    binaire = []
    c = mangos_HP

    if snakeEyes_coolDown == 0:
        while c > 0:
            binaire.append(str(c % 2))
            c //= 2   
        for i in binaire:
            if i == "1":
                a += 1
        if a <= 1:
            mangos_HP = mangos_HP - peter_DP
            peter_HP = peter_HP + peter_DP
    
