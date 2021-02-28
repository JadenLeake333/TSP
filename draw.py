import pygame
import sys

def initialize_board(data,shortest_path,cycle):
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    size = data['width']+100, data['height']+100
    screen = pygame.display.set_mode(size)
    red = (255,0,0)
    white = (255,255,255)
    green = (0,255,0)
    for points in data['nodes']:
        point = pygame.draw.circle(screen,green,(points['x'],points['y']),10)
        point_id = my_font.render(str(points['id']),False,white)
        pygame.Surface.blit(screen, point_id, (points['x']-5, points['y']-5))

    num = data['num']
    if cycle == 'True':
        num += 1
        
    for i in range(num):
        for j in range(len(data['edges'])): #Drawing more times than necessary
            target = data['edges'][j]['target']

            if shortest_path[i] == data['edges'][j]['source'] and target == shortest_path[i+1]:
                idx = shortest_path[i]
                target == shortest_path[i+1]
                x,y = data['nodes'][idx]['x'],data['nodes'][idx]['y']
                x2,y2 = data['nodes'][target]['x'],data['nodes'][target]['y']
                point = pygame.draw.line(screen,green,(x,y),(x2,y2),3)

            elif shortest_path[i+1] == data['edges'][j]['source'] and target == shortest_path[i]:
                idx = shortest_path[i+1]
                target == shortest_path[i]
                x,y = data['nodes'][idx]['x'],data['nodes'][idx]['y']
                x2,y2 = data['nodes'][target]['x'],data['nodes'][target]['y']
                point = pygame.draw.line(screen,green,(x,y),(x2,y2),3)

            else:
                x,y = data['nodes'][i]['x'],data['nodes'][i]['y']
                x2,y2 = data['nodes'][target]['x'],data['nodes'][target]['y']
                point = pygame.draw.line(screen,red,(x,y),(x2,y2),1)

        


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        pygame.display.flip()
