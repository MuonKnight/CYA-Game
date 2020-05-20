#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Character Information#
name = input("Enter your character name: ")
gender = input("What gender are you? ")
race = input("What race are you? ")
align = input("What alignment are you? ")
gold = 0
#Alignment Function#
align_dict = {'lawful good': 1, 'neutral good':2,'chaotic good':3,'lawful neutral':4,'true neutral':5,'chaotic neutral':6,'lawful evil':7,'neutral evil':8,'chaotic evil':9}
align = align.lower()
true_align = align_dict.get(align)

#Stats/Attributes#
stats = {}
import random
min = 3
min2 = 0
max = 20
Strength = random.randint(min,max)
Constitution = random.randint(min,max)
Dexterity = random.randint(min,max)
Intelligence = random.randint(min,max)
Wisdom = random.randint(min,max)
Charisma = random.randint(min,max)
stats = {'Strength':Strength,'Constitution':Constitution,'Dexterity':Dexterity,'Intelligence':Intelligence,'Wisdom':Wisdom,'Charisma':Charisma}
print("Your stats for this game are:",stats)
print("************************************************************************************************************************************")

#Origins#
print("You have been spending the past couple of summer nights at a local tavern drinking and chatting with the locals.")

#Beginning# 
print("You find yourself awake in the familiar room you had been sleeping in, though everything seems foggy.") 
print("You cannot seem to recall how, or when, you fell asleep.")

#Perception Check 1#
p_check1 = 13
wisdom_mod = (stats.get('Wisdom')-10)/2
p_check_act = input("Would you like to investigage the room? (y/n) ")
if p_check_act == 'y':
    roll1 = random.randint(min2,max)+wisdom_mod
    if roll1 >= p_check1:
        print("Your investigation attempt succeeds.")
        print("You feel as though some force is permeating into your room from outside. It's cold.")
        print("The regular chatter of the tavern is nonexistant.")
        p_check_status = 1
    elif roll1 <= 0:
        print("You fall back asleep.")
        p_check_status = -1
    elif roll1 < p_check1:
        print("You find nothing of significance.")
        p_check_status = 0

elif p_check_act =='n':
    print("You decide not to investigate the room.")
    p_check_status = 0

#Perception Check Follow-Up 1#
if p_check_status == 1:
    print("You stand up and gather yourself and your gear, making sure to grab the coinpurse in the nightstand (+50g).")
    gold = gold + 50
    weapon = input("What weapon did you bring? ")
    print("You draw your " + weapon + " and make your way to the door of your room.")
    print("You slowly open the door and make your way past the barren, opened rooms of the tavern.")
#Stealth Check 1#
    stealth_check = 14
    dex_mod = (stats.get('Dexterity')-10)/2
    stealth_check_act = input("You feel an opportunity to sneak here. Would you like to sneak? (y/n) ")
    if stealth_check_act == 'y':
        stealth_roll1 = random.randint(min2,max)+dex_mod
        if stealth_roll1 >=stealth_check:
            print("Your sneak attempt succeeds.")
            print("With the shadows at your side you easily slide by the guarding skeleton, though it appears to be the only one in sight.")
            sneak_attack_check = 9
            skel1_health = 2*random.randint(0,8)+4
            snk_attack_act = input("You could get an attack off on the skeleton without it noticing. (y/n) ")
            if snk_attack_act == 'y':
                while skel1_health > 0:
                    snk_roll = random.randint(min2,max)+dex_mod
                    if snk_roll >= stealth_check:
                        print("Your sneak attack succeeds!")
                        atk_roll1 = 2*abs(2*random.randint(0,8)+dex_mod)
                        skel1_health = skel1_health - atk_roll1
                        if skel1_health > 0:
                            print("The beast, somehow, remains standing!")
                        if skel1_health <= 0:
                            print("The skeleton crumbles under your blow. You found one boneshard.")
                            print("Upon ending the skeleton, you move towards the tavern exit.")
                            print("DEMO END")
                            #quit()
                    if snk_roll < stealth_check:
        #Failed Stealth Attack Phase#
                        print("Your attack misses entirely.")
                        print("The skeleton, now knowing where you are, begins its approach.")
                        skel1_health = 2*random.randint(0,8)+4
                        str_check1 = 10
                        str_mod =(stats.get('Strength')-10)/2
                        print("You have no choice but to attack!")
                        while skel1_health > 0:
                            roll2 = random.randint(min2,max)+str_mod
                            if roll2 >= str_check1:
                                print("Your attack connects!")
                                atk_roll1 = abs(2*random.randint(0,6)+str_mod)
                                skel1_health = skel1_health - atk_roll1 
                                if skel1_health > 0: 
                                    print("The beast takes the hit though as it's approach is relentless.")
                                if skel1_health <=0: 
                                    print("You have vanquished the thieving undead. You found one boneshard.")
                                    print("Upon slaying the undead, you take your trophy and leave the tavern.")
                                    print("DEMO END")
                                    #quit()
                            if roll2 < str_check1:
                                print("Your attack misses and the beast gains ground.")
            elif snk_attack_act =='n':
                print("You decide to sneak past the skeleton, sparing its undead life for another day.")
                print("You sneak out of the tavern without a creak of the floorboards.")
                print("DEMO END")
                #quit()
        #Failed Stealth Attack Phase#
        elif stealth_roll1 < stealth_check:
            print("Your sneak attempt fails. The skeleton takes notice to you.")
            skel1_health = 2*random.randint(0,8)+4
            str_check1 = 10
            str_mod =(stats.get('Strength')-10)/2

            print("You have no choice but to attack!")
            while skel1_health > 0:
                roll2 = random.randint(min2,max)+str_mod
                if roll2 >= str_check1:
                    print("Your attack connects!")
                    atk_roll1 = abs(2*random.randint(0,6)+str_mod)
                    skel1_health = skel1_health - atk_roll1 
                    if skel1_health > 0: 
                        print("The beast takes the hit though as it's approach is relentless.")
                    if skel1_health <=0: 
                        print("You have vanquished the thieving undead. You found one boneshard.")
                        print("You slay the skeleton, taking your trophy, and moving out toward the rest of the village.")
                        print("DEMO END")
                        #quit()
                if roll2 < str_check1:
                    print("Your attack misses and the beast gains ground.")
    if stealth_check_act == 'n':
        print("You decide not to stealth, causing the skeleton to take notice of you. You must attack!")
        skel1_health = 2*random.randint(0,8)+4
        str_check1 = 10
        str_mod =(stats.get('Strength')-10)/2
        while skel1_health > 0:
            roll2 = random.randint(min2,max)+str_mod
            if roll2 >= str_check1:
                print("Your attack connects!")
                atk_roll1 = abs(2*random.randint(0,6)+str_mod)
                skel1_health = skel1_health - atk_roll1 
                if skel1_health > 0: 
                    print("The beast takes the hit though as it's approach is relentless.")
                if skel1_health <=0: 
                    print("You have vanquished the thieving undead. You found one boneshard.")
                    print("You step over the crumbled bones beneath you and approach the exit of the tavern.")
                    print("DEMO END")
                    #quit()
            if roll2 < str_check1:
                print("Your attack misses and the beast gains ground.")
        
elif p_check_status == 0:
    print("You stand up and gather yourself and your gear.")
    weapon = input("What weapon did you bring? ")
    print("You sheath your " + weapon + " and make your way to the door of your room.")
    print("Upon leaving the room you and a skeleton make... eye contact? Causing the skeleton to rush you.")
    print("You have no choice but to attack!")
    skel1_health = 2*random.randint(0,8)+4
    str_check1 = 10
    str_mod =(stats.get('Strength')-10)/2
    while skel1_health > 0:
            roll2 = random.randint(min2,max)+str_mod
            if roll2 >= str_check1:
                print("Your attack connects!")
                atk_roll1 = abs(2*random.randint(0,6)+str_mod)
                skel1_health = skel1_health - atk_roll1 
                if skel1_health > 0: 
                    print("The beast takes the hit though as it's approach is relentless.")
                if skel1_health <=0: 
                    print("You have vanquished the thieving undead. You found one boneshard.")
                    print("You step over the crumbled bones beneath you and approach the exit of the tavern.")
                    print("DEMO END")
                    #quit()
    
elif p_check_status == -1:
    print("You wake up in a panic to the sounds of rattling bones.")
    print("You just finish wiping your eyes when the cold, lifeless fingers of a skeleton begins going through your belongings.")
    print("There is no time to wait " + name + ", you must act now!")
    
#Mid-Event Combat 1#
    skel1_health = 2*random.randint(0,8)+4
    str_check1 = 10
    str_mod =(stats.get('Strength')-10)/2
    str_check_act = input("Will you strike this foul monstrosity? (y/n) ")
    if str_check_act == 'y':
        while skel1_health > 0:
            roll2 = random.randint(min2,max)+str_mod
            if roll2 >= str_check1:
                print("Your attack connects!")
                atk_roll1 = abs(2*random.randint(0,6)+str_mod)
                skel1_health = skel1_health - atk_roll1 
                if skel1_health > 0: 
                    print("The beast takes the hit though as it's approach is relentless.")
                if skel1_health <=0: 
                    print("You have vanquished the thieving undead. You found one boneshard.")
                    print("Upon killing the undead you find your weapon in the closet.")
                    weapon = input("What weapon did you bring?" )
                    print("You sheath your " + weapon + " and move past the barren, opened tavern rooms to the exit.")
                    print("DEMO END")
                    #quit()
            if roll2 < str_check1:
                print("Your attack misses and the beast gains ground.")
#Possible Ending#
    elif str_check_act =='n':
        print("For... whatever reason you have conjured, you decide the best course of action is to stay completely still as the skeleton realizes you are alive and promptly beats you to death.")
        print("You died.")
        #quit()
                
        
            



# In[ ]:




