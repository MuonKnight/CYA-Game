###CYO ADVENTURE GAME###
game_status = False

while game_status == False:
    begin = input("Would you like to begin the game? (y/n) " )
    if begin == 'y':
        #Character Information#
        name = input("Enter your character name: ")
        gender = input("What gender are you? ")
        race = input("What race are you? ")
        align = input("What alignment are you? ")
        inventory_dict = {}
        game_status = True


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
                input("Press 'Enter' to continue.")
                print("You feel as though some force is permeating into your room from outside. It's cold.")
                print("The regular chatter of the tavern is nonexistant.")
                p_check_status = 1
            elif roll1 <= 0:
                print("You fall back asleep.")
                input("Press 'Enter' to continue.")
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
            inventory_dict['gold'] = 50
            weapon = input("What weapon did you bring? ")
            print("You draw your " + weapon + " and make your way to the door of your room.")
            inventory_dict['weapon'] = weapon
            print("You slowly open the door and make your way past the barren, opened rooms of the tavern.")

        #Stealth Check 1#
            stealth_check = 14
            dex_mod = (stats.get('Dexterity')-10)/2
            stealth_check_act = input("You feel an opportunity to sneak here. Would you like to sneak? (y/n) ")
            if stealth_check_act == 'y':
                stealth_roll1 = random.randint(min2,max)+dex_mod
                if stealth_roll1 >=stealth_check:
                    print("Your sneak attempt succeeds.")
                    input("Press 'Enter' to continue.")
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
                                    inventory_dict['boneshard'] = 1
                                    input("Press 'Enter' to continue.")
                                    print("Upon ending the skeleton, you move towards the tavern exit.")
                                    #print("DEMO END")    
                            if snk_roll < stealth_check:

                #Failed Stealth Attack Phase#
                                print("Your attack misses entirely.")
                                print("The skeleton, now knowing where you are, begins its approach.")
                                skel1_health = 2*random.randint(0,8)+4
                                str_check1 = 10
                                str_mod =(stats.get('Strength')-10)/2
                                print("You have no choice but to attack!")
                                input("Press 'Enter' to continue.")
                                while skel1_health > 0:
                                    roll2 = random.randint(min2,max)+str_mod
                                    if roll2 >= str_check1:
                                        print("Your attack connects!")
                                        atk_roll1 = abs(2*random.randint(0,6)+str_mod)
                                        skel1_health = skel1_health - atk_roll1 
                                        if skel1_health > 0: 
                                            print("The beast takes the hit though as its approach is relentless.")
                                        if skel1_health <=0: 
                                            print("You have vanquished the thieving undead. You found one boneshard.")
                                            inventory_dict['boneshard'] = 1
                                            input("Press 'Enter' to continue.")
                                            print("Upon slaying the undead, you take your trophy and leave the tavern.")
                                            #print("DEMO END")
                                    if roll2 < str_check1:
                                        print("Your attack misses and the beast gains ground.")
                    elif snk_attack_act =='n':
                        print("You decide to sneak past the skeleton, sparing its undead life for another day.")
                        input("Press 'Enter' to continue.")
                        print("You sneak out of the tavern without a creak of the floorboards.")
                        #print("DEMO END")
                
                #Failed Stealth Attack Phase#
                elif stealth_roll1 < stealth_check:
                    print("Your sneak attempt fails. The skeleton takes notice to you.")
                    skel1_health = 2*random.randint(0,8)+4
                    str_check1 = 10
                    str_mod =(stats.get('Strength')-10)/2
                    print("You have no choice but to attack!")
                    input("Press 'Enter' to continue.")
                    while skel1_health > 0:
                        roll2 = random.randint(min2,max)+str_mod
                        if roll2 >= str_check1:
                            print("Your attack connects!")
                            atk_roll1 = abs(2*random.randint(0,6)+str_mod)
                            skel1_health = skel1_health - atk_roll1 
                            if skel1_health > 0: 
                                print("The beast takes the hit though as its approach is relentless.")
                            if skel1_health <=0: 
                                print("You have vanquished the thieving undead. You found one boneshard.")
                                inventory_dict['boneshard'] = 1
                                input("Press 'Enter' to continue.")
                                print("You slay the skeleton, taking your trophy, and move out toward the rest of the village.")
                                #print("DEMO END")
                        if roll2 < str_check1:
                            print("Your attack misses and the beast gains ground.")
            if stealth_check_act == 'n':
                print("You decide not to stealth, causing the skeleton to take notice of you. You must attack!")
                input("Press 'Enter' to continue.")
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
                            print("The beast takes the hit though as its approach is relentless.")
                        if skel1_health <=0: 
                            print("You have vanquished the thieving undead. You found one boneshard.")
                            inventory_dict['boneshard'] = 1
                            input("Press 'Enter' to continue.")
                            print("You step over the crumbled bones beneath you and approach the exit of the tavern.")
                            #print("DEMO END")  
                    if roll2 < str_check1:
                        print("Your attack misses and the beast gains ground.") 
        elif p_check_status == 0:
            print("You stand up and gather yourself and your gear.")
            weapon = input("What weapon did you bring? ")
            print("You sheath your " + weapon + " and make your way to the door of your room.")
            inventory_dict['weapon'] = weapon
            print("Upon leaving the room you and a skeleton make eye contact? Causing the skeleton to rush you.")
            print("You have no choice but to attack!")
            input("Press 'Enter' to continue.")
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
                            print("The beast takes the hit though as its approach is relentless.")
                        if skel1_health <=0: 
                            print("You have vanquished the thieving undead. You found one boneshard.")
                            inventory_dict['boneshard'] = 1
                            input("Press 'Enter' to continue.")
                            print("You step over the crumbled bones beneath you and approach the exit of the tavern.")
                            #print("DEMO END")
        elif p_check_status == -1:
            print("You wake up in a panic to the sounds of rattling bones.")
            print("You just finish wiping your eyes when the cold, lifeless fingers of a skeleton begins going through your belongings.")
            print("There is no time to wait " + name + ", you must act now!")
            input("Press 'Enter' to continue.")
            
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
                            print("The beast takes the hit though as its approach is relentless.")
                        if skel1_health <=0: 
                            print("You have vanquished the thieving undead. You found one boneshard.")
                            inventory_dict['boneshard'] = 1
                            input("Press 'Enter' to continue.")
                            print("Upon killing the undead you find your weapon in the closet.")
                            weapon = input("What weapon did you bring?" )
                            print("You sheath your " + weapon + " and move past the barren, opened tavern rooms to the exit.")
                            inventory_dict['weapon'] = weapon
                            #print("DEMO END")
                    if roll2 < str_check1:
                        print("Your attack misses and the beast gains ground.")

        #Possible Ending#
            elif str_check_act =='n':
                print("For... whatever reason you have conjured, you decide the best course of action is to stay completely still as the skeleton realizes you are alive and promptly beats you to death.")
                print("You died.")
                quit()   
        #Out of the Tavern (Stealth Check = 1)#
        smith_check = input("You exit the tavern and look around. Surrounding you is buildings, ones mostly in ruins, and you see an operating smithy. Would you like to go? (y/n) ")
        if smith_check == 'y':
            upgrade_1 = input("You walk to the smithy and remember the boneshard you picked up earlier. Would you like to use it? (y/n) ")
            if upgrade_1 =='y':
                if inventory_dict['boneshard'] == 1:
                    print("You use the boneshard to upgrade your weapon, making it a bone " + weapon + ". You put it away and leave the smithy.")
                    weapon = 'bone ' + weapon
                    inventory_dict['weapon'] = weapon
                    inventory_dict['boneshard'] = 0
            if upgrade_1 =='n':
                print("You elect not to use the boneshard. Seeing no other reason to stick around, you leave the smithy.")
        elif smith_check == 'n':
            print("You see no reason to go to the smithy and look elsewhere beyond the town.")
        print("You look back one more time upon the town and watch the flames devour the last pieces.")
        print("You finally begin your march out of the town and into the heavily wooded trails.")
        print("********************************************************************************")
        input("Press 'Enter' to continue.")
        print("After traveling for some time you come across a man sitting at the fork in the path ahead.")
        print("As you get closer, the man looks up.")
        print("What's a blasted " + race + " like you doing in these woods?")
        wood_dialogue = 0
        while wood_dialogue == 0:
            print("***DIALOGUE OPTIONS***")
            print("1. What have you got against my race?")
            print("2. I'm just looking for a way through these woods.")
            print("3. What's a blasted man like you doing in these woods?")
            print("4. Hold your tongue unless you wish to lose it.")
            wood_option = int(input("Select a number 1-4. "))
            if wood_option == 1:
                print("Never liked your kind. Bring trouble wherever you go.")
                input("Press 'Enter' to continue.")
            elif wood_option == 2:
                print("Both paths will take you from these woods, though the journey differs.")
                print("If you're looking for the safest path by the gods stay on the right one.")
                print("Though if you think you're strong... then take the left.")
                input("Press 'Enter' to continue.")
                wood_dialogue = 1
            elif wood_option == 3:
                print("Hiding from what happened from the village not too far from here.")
                input("Press 'Enter' to continue.")
            elif wood_option == 4:
                print("That's no way to talk to your elder man.")
                input("Press 'Enter' to continue.")
        print("You realize now you have a choice to make.")
        wooded_path = int(input("Will you go down the right or left path? (1 = Right|2 = Left) "))
        if wooded_path == 1:
            print("With the choice seeming almost too obvious, you take the path on the right.")
            print("You walk around a mile or so before a thought strikes you.")
            print("You feel as though something is off. Considering the village this seems too calm.")
            wood_per = 20
            wood_per_check = input("You could investigate your surroundings. Would you like to? (y/n) ")
            if wood_per_check == 'y':
                roll_wood = random.randint(min2,max)+wisdom_mod
                if roll_wood >= wood_per:
                    print("Your investigation succeeds.")
                    input("Press 'Enter' to continue.")
                    print("You detect an awful, slurping beast in the distance and what appears to sound like dissolving bones.")
                    wood_beast = input("You could go see what this is or you could ignore it and move on. Would you like to check what it is? (y/n) ")
                    if wood_beast == 'y':
                        print("Without a moment to hesitate you run off towards the sounds, the muck of the woods growing deeper around your feet.")
                        print("You run for three minutes and yet you don't see anything close to the beast you heard earlier.")
                        print("Suddenly, after running in the muck, you hear the dissolving sensation again, not from afar, though, as the sound is coming from you!")
                        input("Press 'Enter' to continue.")
                        print("All of the time you spent 'courageously' running into the muck, you failed to realize it was the muck that was the real monster.")
                        print("You died.")
                        quit()
                    elif wood_beast == 'n': 
                        print("You decide to ignore the sounds, remembering you have more important things to do.")
                elif roll_wood < wood_per:
                    print("Your investigation attempt fails.")
                    input("Press 'Enter' to continue.")
                    print("You continue on as if you had never tried to see anything.")
        if wooded_path == 2:
            print("You swallow what could be the lost drop of not-blood you have for a while as you prepare to go down the left path.")
            print("You look back behind you, memorizing what feels like the last peaceful scene you might see, ready your weapon, and set on the path.")
                








        


















































        again = input("Would you like to go again? (y/n) ") 
        if again == 'y':
             game_status = False
        else:
            print("Goodbye.")
            quit()
        
    elif begin == 'n':
        print('Goodbye.')
        quit()
        


