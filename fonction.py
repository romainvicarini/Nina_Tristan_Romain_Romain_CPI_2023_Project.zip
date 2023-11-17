import random


def peter_normal_damage() :
    global peter_DP_list
    peter_DP=random.choice(peter_DP_list) #give a random attack value of Peter
    return peter_DP

def mangos_normal_damage():
    global mangos_DP_list
    mangos_DP=random.choice(mangos_DP_list) #give a random attack value of mangos
    return mangos_DP

def mangos_turn():
    global peter_HP,peter_armor_HP,peter_DP, mangos_DP
    mangos_damage= mangosNormalDamage()
    mangos_DP = mangos_damage - peter_armor_HP
    peter_HP= peter_HP - mangos_DP
    print ("ouch ! the mangos attacks you, you lost",mangos_DP,"HP")
    print("you have",peter_HP,"HP left")
    return

def peter_normal_turn():
   
        global mangos_armor_hp,mangos_HP,peter_DP
        peter_damage = peterNormalDamage()
        peter_DP= peter_damage - mangos_armor_HP
        mangos_HP= mangos_HP - peter_DP
        print("you inflicted",peter_DP,"damage to the mongose !")
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

def last_chance_attack(peter_HP, damage):
    if not hasattr(last_chance_attack, 'used') or not last_chance_attack.used:
        percentage_lost = (20 - peter_HP) / 20 * 100
        chance_of_success = min(percentage_lost, 100)
        if random.uniform(0, 100) < chance_of_success:
            # Hit
            damage_dealt = damage * 3
            print("Last chance attack hits! Dealing", damage_dealt, "damage.")
            last_chance_attack.used = True  # Mark last chance attack as used
            return damage_dealt
        else:
            # Miss
            print("Last chance attack misses!")
            last_chance_attack.used = True  # Mark last chance attack as used
            return 0
    else:
        print("Last chance attack has already been used in this fight.")
        return 0
