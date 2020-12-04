from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
import time


def update_visual(screen: Screen, inputs: list[int], cursor_one: int, cursor_two: int):
    x, y, index = 0, 0, 0
    row = 20
    for number in inputs:

        if cursor_one == index:
            bg = 3
            colour = 0
        elif cursor_two == index:
            bg = 13
            colour = 0
        else:
            bg = 0
            colour = 10

        screen.print_at(text=f'{number}', x=x, y=y, colour=colour, bg=bg)

        index += 1
        if (index % row) == 0:
            y = 0
            x += 7
        else:
            y += 1
    screen.refresh()


def day1_1(screen):
    inputs = [int(x) for x in open(
        "/Users/ciaran.whyte/dev/aoc2020/day1/input.txt").read().splitlines()]

    for idx, num in enumerate(inputs):
        c_one = idx
        for idx_two, c_two in enumerate(inputs[idx:]):
            update_visual(screen, inputs, c_one, idx+idx_two)
            
            if c_two + num == 2020:
                # centre = (screen.width // 2, screen.height // 2)
                # screen.print_at(text=f"{num} + {c_two} == 2020", x=centre[0], y=centre[1], colour=0, bg=13)
                # screen.print_at(text=f"{num} * {c_two} == {num * c_two}", x=centre[0]+1, y=centre[0]+1, colour=3, bg=0)
                # screen.refresh()
                # screen.close()
                effects = [
                    Cycle(
                        screen,
                        FigletText(f"{num} + {c_two} == 2020", font='big'),
                        int(screen.height / 2 - 8)),
                    Cycle(
                        screen,
                        FigletText(f"{num} * {c_two} == {num * c_two}", font='big'),
                        int(screen.height / 2 + 3)),
                    Stars(screen, 200)
                ]
                screen.play([Scene(effects, 500)])
                time.sleep(5)
                return


Screen.wrapper(day1_1)
