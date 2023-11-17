import random
peter_DP_list=[3,4,5,6,]
peter_HP=20
peter_armor_HP=1
mangos_HP=10

def peter_normal_damage() :
            peter_DP=random.choice(peter_DP_list) #give a random attack value of Peter

def peter_normal_turn():
        global mangos_armor_hp,mangos_HP,peter_DP
        peter_damage = peterNormalDamage()
        peter_DP= peter_damage - mangos_armor_HP
        mangos_HP= mangos_HP - peter_DP
        print("you inflicted",peter_DP,"damage to the mongose !")
        print("the mangos still have",mangos_HP,"HP")
        return

def snakeEyes():
    global mangos_HP, peter_HP,snakeEyes_coolDown
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
            peter_normal_turn()
            peter_HP = peter_HP + peter_DP
            print ("you regained",peter_DP,"HP")
            print("you have now",peter_HP,"HP")
        else:
            peter_normal_turn()
        snakeEyes_coolDown=+ 2
    else:
        print("still in cooldown, please choose an other attack")

def special_attack(b):
            while b!=0 and b!=1 and b!=2 and b!=3:
                        print("Invalid choice. Please enter a valid option.")
                        a=int(input("Choose your special attack: \n Defend: enter 1 \n Snake eyes: enter 2 \n Last chance: enter 3 \n If you want to go back to regular attack: enter 0\n"))
            if b==0:
                        peter_normal_turn()
            elif b==1: #Defend: armorPV *2 + regular attack
                        peter_armor_HP = peter_armor_HP*2
                        if peter_HP%2==0:
                                    peter_normal_turn()
                        print("Peter's armor is now", peter_armor_HP, "\n")
            elif b==2: #Snake eyes: regular attack + DP inflicted = DP gained => fonction 'bin'
                        snake_eyes()
            elif b==3: #Last chance: DP max *3 but sometimes miss the target
                        mangos_hp = mangos_hp-(peter_DP_list[3]*3) #hits for maximum damage multiplied by 3
        
        print("Executing a special attack, Peter inflicted", peter_DP, "\n")

a=int(input("Oh no! A mangoose is coming.\nStart of the fight, choose your attack:\nNormal attack: enter 0\nSpecial attack: enter another value\n"))
def attack(a):
            if a==0:
                        peter_normal_turn()
            else:
                        b=int(input("Choose your special attack: \n Defend: enter 1 \n Snake eyes: enter 2 \n Last chance: enter 3 \n If you want to go back to regular attack: enter 0\n")      
                        special_attack(b)
attack(a)

#nex time, continuer le combat tant que aucun est mort
