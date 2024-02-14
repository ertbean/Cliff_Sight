from cave import cavemod
from random import randint
from asciimatics.effects import Print, Stars
from asciimatics.particles import Explosion, StarFirework, DropScreen, Rain, ShootScreen
from asciimatics.renderers import SpeechBubble, FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys
from pygame import mixer



def demo(screen):
    screen.set_title("Cliff Sight - Game")

    scenes = []

    # First scene: title page
    effects = [
        Print(screen,
              Rainbow(screen, FigletText("Cliff Sight", font="big")),
              y=screen.height // 4 - 5),   
        Print(screen,
              SpeechBubble("Press SPACE to Start..."),
              screen.height - 3,
              transparent=False,
              start_frame=1)       
        ]
    scenes.append(Scene(effects, -1))

    # Next scene: just dissolve the title.
    effects = []
    for i in range(8):
        effects.append(ShootScreen(
            screen,
            randint(screen.width // 3, screen.width * 2 // 3),
            randint(screen.height // 4, screen.height * 3 // 4),
            100,
            diameter=randint(8, 12),
            start_frame=i * 10))
    effects.append(ShootScreen(
            screen, screen.width // 2, screen.height // 2, 100, start_frame=1))
    scenes.append(Scene(effects, 20, clear=False))

    # Next scene: sub-heading.
    effects = [
        DropScreen(screen, 100),
        Print(screen,
              Rainbow(screen, FigletText("Prologue", font="doom")),
              y=screen.height // 2 - 5,
              stop_frame=30),
        DropScreen(screen, 100, start_frame=30)
    ]
    scenes.append(Scene(effects, 80))

    # Next scene: Prologue
    effects = [
    Rain(screen, 120),
    Print(screen,
              SpeechBubble("One fateful day the elves arrived. During their time on a small planet they dubbed second world they stole all sight from the inhabitance and suspended all Powerful Ones in time."),
              y=screen.height // 2 - 5,
              speed=1,
              transparent=False,
              stop_frame=120),
    ]

    scenes.append(Scene(effects, -1))

    screen.play(scenes, stop_on_resize=False)







while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError:
        pass 










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

                                                                      
                                                               
