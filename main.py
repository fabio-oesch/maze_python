import pygame
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from vector import Vector


def main():
    vec1 = Vector(1,1)
    print(vec1)
    print(vec1.magnitude())
    print(vec1.norm())
    print(vec1.norm().magnitude())
    vec2 = Vector(-1,-1)
    print(vec1 + vec2)
    vec1.scalar_mul(5)
    print(vec1)
    frame = simplegui.create_frame('this frame', 400, 400)
    frame.start()


if __name__ == "__main__":
    main()
