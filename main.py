"""
Problem 1 - Karel’s Home
"""
from stanfordkarel import *


def main():
    move_to_package()
    return_to_starting_point()


def move_to_package():
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()


def return_to_starting_point():
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


# don't change this code
if __name__ == '__main__':
    run_karel_program()


