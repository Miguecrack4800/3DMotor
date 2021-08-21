import pygame
from Engine import Engine
from Player import Player
from GameObject import GameObject
from Camera import Camera

pygame.init()

screensize = (1280, 720)
screen = pygame.display.set_mode(screensize)

camera = Camera()
player = Player(camera, (0,0,0))
player.tick()
clk = pygame.time.Clock()
eng = Engine(screen, screensize, camera)
run = True
while run:
    print(clk.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((250, 250, 250))

    #eng.draw_plane(eng.get_plane([(0,2,1), (1,2,1), (1,1,1), (0,1,1)]), (0, 0, 0), None)

    eng.draw_plane(eng.get_plane([(0, 1, 1), (0, 1, 2), (0, 2, 2), (0, 2, 1)]), (0, 250, 0), None)
    eng.draw_plane(eng.get_plane([(1, 1, 1), (1, 1, 2), (1, 2, 2), (1, 2, 1)]), (0, 250, 0), None)
    eng.draw_plane(eng.get_plane([(0, 2, 1.5), (1, 2, 1.5), (1, 2, 1), (0, 2, 1)]), (250, 0, 0), None)
    eng.draw_plane(eng.get_plane([(0, 1, 2), (1, 1, 2), (1, 2, 2), (0, 2, 2)]), (250, 0, 0), None)
    eng.draw_plane(eng.get_plane([(0, 1, 2), (1, 1, 2), (1, 1, 1), (0, 1, 1)]), (0, 0, 250), None)

    for y in range(21):
        for x in range(101):
            eng.draw_point((0 + x * 0.01, 1 + 0.05*y, 1), (255, 255, 0))


    pygame.display.flip()
    clk.tick()