import pygame
import sys

def initialize_board(**kwargs):
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    size = kwargs['width']+100, kwargs['height']+100
    screen = pygame.display.set_mode(size)
    red = (255,0,0)
    white = (255,255,255)
    green = (0,255,0)
    for points in kwargs['nodes']:
        point = pygame.draw.circle(screen,green,(points['x'],points['y']),10)
        point_id = my_font.render(str(points['id']),False,white)
        pygame.Surface.blit(screen, point_id, (points['x']-5, points['y']-5))
    
    for i in range(kwargs['num']):
        for j in range(len(kwargs['edges'])):
            if i == kwargs['edges'][j]['source']:
                target = kwargs['edges'][j]['target']
                x,y = kwargs['nodes'][i]['x'],kwargs['nodes'][i]['y']
                x2,y2 = kwargs['nodes'][target]['x'],kwargs['nodes'][target]['y']
                point = pygame.draw.line(screen,red,(x,y),(x2,y2),1)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        pygame.display.flip()
