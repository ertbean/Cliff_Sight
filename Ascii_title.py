#!/usr/bin/env python3

from random import randint
from asciimatics.effects import Print, Stars
from asciimatics.particles import Explosion, StarFirework, DropScreen, Rain, ShootScreen
from asciimatics.renderers import SpeechBubble, FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys
from pygame import mixer

from place1 import main 


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


main()




while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError:
        pass 
