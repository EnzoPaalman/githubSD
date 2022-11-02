from time import sleep


print("Welcome to Night City.")
sleep(1)
print("This game is about a Cyberpunk themed city/world.")
sleep(4)
print("The year is 2077, After extreme global warming, the fall of the first internet and the 3rd world war.")
sleep(5)
print("The last so called 'city of dreams' is called Night City. The city is around 100 by 110 km, filled with tall futuristic skyscrapers, bright colored lights, commercials everywhere and flying cars.")
sleep(3)
print("But one thing is very clear when you arrive in Night City, its not a city of dreams.")
sleep(5)
print("Filled with gang wars and a corrupt mega corporation named Arasaka that rules the city.")
print("Death has become a normal part of life.")
sleep(5)
print("Your character backstory:")
sleep(2)
print("Your character used to be a nomad (someone who lives in the desert with his gang).")
sleep(5)
print("After countering a cyberware transport convoy, you betray your gang for a piece of military grade cyberware named The Sandevistan. ")
sleep(5)
print("The Sandevistan is one of the most powerfull pieces of cyberware in the world.")  
print("It grants you the ability to go super speed, slowing down the world around you.")
sleep(5)
print("After betraying your gang you need a place to hide.")
sleep(3)
print("You decide to go to Nightcity.")
sleep(3)
print("Its time to choose your characters name.")
sleep(3)


name = input("Enter Name: ")
sleep(2)
print(name + "!" " Good choice.")
sleep(3)


print("You approach the border of night city.")
sleep(3)
print("You look around you, its heavily guarded.")
sleep(3)
print("Do you, ")
print("A: show your passport")
sleep(1)
print("B: try to sneak through")
sleep(3)

choice = input("A/B:  ")
sleep(2)

if choice == 'A':
    print("You hand your passport to the arasaka agent.")
    sleep(2)
    print("He looks at your passport then looks at a different agent.")
    sleep(3)
    print("A man in a suit appears and asks for you to come with him.")
    sleep(2)
    print("do you")
    print("A: Come with him")
    print("B: Run for it")
    sleep(2)
    

    choice = input("A/B/C:  ")
    sleep(2)


    if choice == 'A':
        print("You follow him into an interogation room.")
        sleep(3)
        print("Suited man: We know you have military grade cyberware.")
        sleep(3)
        print("Suited man: Its quite impresive that you aren't dead yet, this type of cyberware would fry a humans brain instantly.")
        sleep(5)
        print("Suited man: We would like to offer you a deal.")
        sleep(3)
        print("Suited man: We would like to run some tests on you.")
        sleep(3)
        print("Suited man: In return we will offer you a job at Arasaka, and a greencard for NightCity.")
        sleep(3)
        print("Do you,")
        sleep(3)
        print("A: take the deal")
        print("B: Decline offer")


        choice = input("A/B:  ")
        sleep(3)

        if choice == 'A':
            print("Suited man: Good choice Mister " + name + ".")
            sleep(3)
            print("Suited man: You are now a resident in NightCity mister " + name + ", congratulations.")
            sleep(3)
            print("Game over.")
            print("Ending 1 of 8")


        elif choice == 'B':
            print("Suited man: Mister " + name + ", We cannot let you leave with The Sandevistan.")
            sleep(3)
            print("You get put into a coma")
            sleep(3)
            print("Game over.")
            print("Ending 2 of 8")
        
        
        else:
            print("Invalid answer")


    elif choice == 'B':
        print("You try to run")
        sleep(2)
        print("Stupid choice")
        print("You get shot by the guards.")
        sleep(3)
        print("Game over.")
        print("Ending 3 of 8")
    
    
    else:
        print("Invalid answer")
        

elif choice == 'B':
    print("You sneak past the border.")
    sleep(3)
    print("A drone notices you, it turns on its alarm notifying the guards.")
    sleep(3)
    print("Do you,")
    print("A:  stop")
    print("B:  activate The Sandevistan")
    sleep(3)

    choice = input("A/B:  ")
    sleep(2)

    if choice == 'A':
        print("You stop")
        sleep(3)
        print("The guards taze you.")
        sleep(3)
        print("You get arrested and sent to prison. Atleast you escaped your gang.")
        sleep(3)
        print("Game over.")
        print("Ending 4 of 8")
    
    
    elif choice == 'B':
        print("You activate The Sandevistan and sprint to the city.")
        sleep(3)
        print("The guards think it was a false alarm.")
        sleep(3)
        print("You're now a fugitive in NightCity.")
        sleep(3)
        print("You start to feel The Sandevistan causing harm to your body.")
        sleep(5)
        print("You start getting flashes of the desert, You are going into a psychosis.")
        sleep(5)
        print("Do you,")
        print("A:  Go to a ripperdoc (A blackmarket cyberware doctor).")
        print("B:  Find a local gang to help you out.")
        sleep(3)


        choice = input("A/B:  ")
        sleep(3)


        if choice == 'A':
            print("You arrive at the ripperdoc's shop.")
            sleep(3)
            print("Ripperdoc: Wassup kid, you need some help?")
            sleep(3)
            print(name + ":" + " I need some medication for cyberpsychosis.")
            sleep(3)
            print("Ripperdoc: Alright kid, im gonna have to see that cyberware.")
            sleep(5)
            print("Ripperdoc: Oh wow, The Sandevistan.")
            sleep(3)
            print("Ripperdoc: How'd you get your hands on that kid.")
            sleep(3)
            print(name + ":" + " None of your business, can you help me or not.")
            sleep(3)
            print("Ripperdoc: Lisen kid, thats one of the most powerfull pieces of cyberware in the city.")
            sleep(3)
            print("Ripperdoc: I cant promise you that the medication will help, but if you want i can buy it off you for a VERY handsome price.")
            sleep(5)
            print("Do you,")
            print("A:  Take the medication")
            print("B:  Sell The Sandevistan")
            sleep(3)


            choice = input("A/B:  ")
            sleep(3)


            if choice == 'A':
                print("Ripperdoc: You've got a deathwish kid.")
                sleep(3)
                print("The medication doesn't work")
                sleep(3)
                print("You end up going cyberpsycho and fry your brain")
                sleep(5)
                print("Game over.")
                print("Ending 5 of 8")
            

            elif choice == 'B':
                print("Ripperdoc: Pleasure doin business with ya kid.")
                sleep(3)
                print("He pays you 1.3mil eurodollars.")
                sleep(3)
                print("Thats enough money to get yourself set up in NightCity.")
                sleep(5)
                print("Congratulations, you got the best ending")
                print("Ending 6 of 8")

            
            
            else:
                print("Invalid answer")
        
        
        elif choice == 'B':
            print("You find a gang hideout.")
            sleep(3)
            print("Gang leader: Wassup kid, What are you doin here.")
            sleep(3)
            print(name + ":" + " Im lookin to join your gang.")
            sleep(3)
            print("Gang leader: HAHAHA, What do you got to offer to the team kid.")
            sleep(5)
            print(name + ":" + " Ive got The Sandevistan.")
            sleep(3)
            print("Gang leader: Oh wow, you're playin with fire kid.")
            sleep(3)
            print("Gang leader: Listen up kid, ill offer you a deal.")
            sleep(3)
            print("Gang leader: You give me The Sandevistan, and we'll take care of ya. deal?")
            sleep(5)
            print("Do you,")
            print("A:  Take the deal")
            print("B:  Decline the offer")
            sleep(3)


            choice = input("A/B:  ")
            sleep(3)


            if choice == 'A':
                print("Gang leader: Good choice kid, welcome to the gang.")
                sleep(3)
                print("Game over.")
                print("Ending 7 of 8")
            

            elif choice == 'B':
                print("Im gonna need that cyberware kid.")
                sleep(3)
                print("You get knocked out, and they take The Sandevistan from you.")
                sleep(3)
                print("Game over.")
                print("Game ending 8 of 8")
        

        else:
            print("Invalid answer")
    
    
    elif choice == 'C':
        print("So anyways, u start blastin.")
        sleep(3)
        print("An alarm gets sent out to militech of an attack on the boarder.")
        sleep(3)
        
        print("Do you:")
        print("A: flee back into the desert")
        sleep(2)
        print("B: keep fighting")
        
        choice = input("A/B:  ")

        if choice == 'A':
            print("You run back into the desert.")
            sleep(3)
            print("Do you")
            sleep(2)
            print("A: Return to your gang.")
            print("B: Game end yourself.")
            
            choice = input("A/B:  ")

            if choice == 'A':
                print("You go back to your gang.")
                sleep(3)
                print("They call you a traitor, they kill you and take the sandevistan.")

        elif choice == 'B':
            print("You keep fighting")
            sleep(3)
            print("But it doesnt go on for long.")
            sleep(5)
            print("Game over.")
            print("secret ending 1/2")


        else:
            print("Invalid answer")


    else:
        print("Invalid answer")
   

else:
    print("Invalid Answer")