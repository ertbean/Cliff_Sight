from cave import cavemod

def main():
        health = 10
        damage5 = "5,f"
        damage4 = "4,f"
        damage3 = "3,f"
        danage2 = "2,f"
        damage1 = "1,f"
        stick = "if used damage1"
        invontory = "stick"
        gameover = "u die"
        explore1 = 'n'
        no = "thats not a option"
        cave = 3
        print('you wake up confused')
        print('you start to think of what to do')
        print('these are the options you thought of. 1 open invontory. 2 look around for things. 3 try to rember what happend prier.4 scout out sourandings. ')
        option = input('press y to continue')
        while not option.lower()== 'y':
                option = input('Press y to continue.')
        while not option.lower()== 'y':
                option = input('Press y to continue.')
                if option.lower()== 'y':
                        break
        while True:
                option1 = input(' Option 1 type 1 type. Something else for no.')
                if option1.lower()== '1' :
                        print( 'You have 1 stick in your invontory.' )
                else: 
                        option2 = input(' option 2 type 2 type something else for no')
                        if option2.lower()== '2' :
                                print('you find nothing interesting')
                        else: 
                                option3 = input('option 3 type 3 type something else for no')
                                if option3.lower()== '3' :
                                        print('you try to rember to no availe')
                                else:
                                        option4 = input('option 4 type 4 type something else for no')
                                        if option4.lower()== '4' :
                                                print('you see nothing but sand the only other thing you see is a cave')
                                                explore1 = input('enter cave y?')
                                        if explore1.lower()== 'y':
                                                        break
                                        if not explore1.lower()== 'y':
                                                        print('redoing opions')
        cavemod()                                      

if __name__ == '__main__':
    main()

                                                                      
                                                               
