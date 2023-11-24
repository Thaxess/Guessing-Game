# A program that tries to guess the number that you are thinking of (1-100) in 5 guesses

from random import randint 


#make it so it will start with 5 guesses
ges = 5
lhg = True

#get the input to start / read tutorial
f_input = input(f"Think of a number in your head 1-100 and press the enter key to start (to read the tutorial type t)  ")

#if the input is t show the tutorial
if f_input.lower() == 't':
    input("""First you think of a number in your head for the game to try to g and then you press enter to start the game.
As the program tries to g the number you will have to tell if the number is lower(l) or higher(h) than the number ged.
thats it. Oh and, if it ges the number you can always type g for ged to finish the game. (press enter to exit)""")
else:
    g50 = input("Hmm i think my first g is gonna be 50! that seems like the best starter. welp, at least for me. [l/h/g]   ")

    if g50.lower() == 'g':
        print('Is it 50? That was easy! you should try again.')

    elif g50.lower() == 'l':
        g25 = input("I'm thinking of 25. [l/h/g] |  ")

        if g25.lower() == 'g':
            print("25 it is! easy tho")
            exit()


        elif g25.lower() == 'l':
            g12 = input("I'm thinking of 12. [l/h/g] |  ")
            
            if g12 == 'g':
                print('12 it is! easyyy.')
                exit

            elif g12 == 'l':
                rnumber1 = randint(1, 11)
                lastguess1 = input(f"I'm thinking of {rnumber1}. [l/h/g] |  ")
                if lastguess1 == 'g':
                    print(f"{rnumber1} it is! easyyy")
                    exit()

                elif lastguess1 == 'l':
                        print(f"This is my last guess... I'll try {randint(0, rnumber1)}")
                        exit()

                elif lastguess1 == 'h':
                        print(f"This is my last guess... I'll try {randint(rnumber1, 11)}")
                        exit()
        
            elif g12 == 'h':
                rnumber2 = randint(13, 24)
                lastguess2 = input(f"I'm thinking of {rnumber2}. [l/h/g] |  ")

                if lastguess2 == 'g':
                    print(f"{rnumber2} it is! easyyy")
                    exit()

                elif lastguess2 == 'l':
                        print(f"This is my last guess... I'll try {randint(13, rnumber2)}")
                        exit()

                elif lastguess2 == 'h':
                        print(f"This is my last guess... I'll try {randint(rnumber2, 23)}")
                        exit()

        elif g25.lower() == 'h':
            g38 = input("I'm thinking of 38. [l/h/g] |  ")

            if g38 == 'g':
                print('38 it is! easyyy.')
                exit()

            elif g38 == 'l':
                rnumber3 = randint(26, 37)
                lastguess3 = input(f"I'm thinking of {rnumber3}. [l/h/g] |  ")

                if lastguess3 == 'g':
                    print(f"{rnumber3} it is! easyyy")
                    exit()

                elif lastguess3 == 'l':
                        print(f"This is my last guess... I'll try {randint(26, rnumber3)}")
                        exit()

                elif lastguess3 == 'h':
                        print(f"This is my last guess... I'll try {randint(rnumber3, 37)}")
                        exit()
        
            elif g38 == 'h':
                rnumber4 = randint(39, 49)
                lastguess4 = input(f"I'm thinking of {rnumber4}. [l/h/g] |  ")

                if lastguess4 == 'g':
                    print(f"{rnumber4} it is! easyyy")
                    exit()

                elif lastguess4 == 'l':
                        print(f"This is my last guess... I'll try {randint(39, rnumber4)}")
                        exit()

                elif lastguess4 == 'h':
                        print(f"This is my last guess... I'll try {randint(rnumber4, 49)}")
                        exit()





    elif g50.lower() == 'h':
        g75 = input("I'm thinking of 75. [l/h/g] |  ")

        if g75 == 'g':
            print('75 it is! easyyy')
            exit()

        if g75 == 'l':
            g63 = input("I'm thinking of 63. [l/h/g] |  ")
            
            if g63 == 'g':
                print('63 it is! easyyy.')
                exit

            elif g63 == 'l':
                rnumber5 = randint(51, 62)
                lastguess5 = input(f"I'm thinking of {rnumber5}. [l/h/g] |  ")

                if lastguess5 == 'g':
                    print(f"{rnumber5} it is! easyyy")
                    exit()

                elif lastguess5 == 'l':
                        print(f"This is my last guess... I'll try {randint(51, rnumber5)}")
                        exit()

                elif lastguess5 == 'h':
                        print(f"This is my last guess... I'll try {randint(rnumber5, 62)}")
                        exit()
        
            elif g63 == 'h':
                rnumber6 = randint(64, 74)
                lastguess6 = input(f"I'm thinking of {rnumber6}. [l/h/g] |  ")

                if lastguess6 == 'g':
                    print(f"{rnumber6} it is! easyyy")
                    exit()

                elif lastguess6 == 'l':
                        print(f"This is my last guess... I'll try {randint(64, rnumber6)}")
                        exit()

                elif lastguess6 == 'h':
                        print(f"This is my last guess... I'll try {randint(rnumber6, 74)}")
                        exit()
        

        if g75 == 'h':
            g88 = input("I'm thinking of 88. [l/h/g] |  ")

            if g88 == 'g':
                print('88 it is! easyyy.')
                exit()

            elif g88 == 'l':
                rnumber7 = randint(76, 87)
                lastguess7 = input(f"I'm thinking of {rnumber7}. [l/h/g] |  ")

                if lastguess7 == 'g':
                    print(f"{rnumber7} it is! easyyy")
                    exit()

                elif lastguess7 == 'l':
                        print(f"This is my last guess... I'll try {randint(76, rnumber7)}")
                        exit()

                elif lastguess7 == 'h':
                        print(f"This is my last guess... I'll try {randint(rnumber7, 87)}")
                        exit()
        
            elif g88 == 'h':
                rnumber8 = randint(89, 99)
                lastguess8 = input(f"I'm thinking of {rnumber8}. [l/h/g] |  ")

                if lastguess8 == 'g':
                    print(f"{rnumber8} it is! easyyy")
                    exit()

                elif lastguess8 == 'l':
                        print(f"This is my last guess... I'll try {randint(89, rnumber8)}")
                        exit()

                elif lastguess8 == 'h':
                        print(f"This is my last guess... I'll try {randint(rnumber8, 99)}")
                        exit()