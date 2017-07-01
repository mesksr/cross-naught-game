import pygame, sys

def check():
    if ((grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2] and grid[0][2] == 'cross') or
        (grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2] and grid[1][2] == 'cross') or
        (grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2] and grid[2][2] == 'cross') or
        (grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0] and grid[2][0] == 'cross') or
        (grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1] and grid[2][1] == 'cross') or
        (grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2] and grid[2][2] == 'cross') or
        (grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[2][2] == 'cross') or
        (grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[2][0] == 'cross')):
        return 1, "Player 1 (Cross) Won"
    elif ((grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2] and grid[0][2] == 'naught') or
          (grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2] and grid[1][2] == 'naught') or
          (grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2] and grid[2][2] == 'naught') or
          (grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0] and grid[2][0] == 'naught') or
          (grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1] and grid[2][1] == 'naught') or
          (grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2] and grid[2][2] == 'naught') or
          (grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[2][2] == 'naught') or
          (grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[2][0] == 'naught')):
        return 1, "Player 2 (Naught) Won"
    elif ('blank' not in grid[0] and 'blank' not in grid[1] and 'blank' not in grid[2]):
        return 1, "Draw"
    else:
        return 0, "Continue"
        
pygame.init()
width, height = 600, 600
size = width, height+30
white = 255, 255, 255
black = 0, 0, 0
counter = 1
grid = [['blank', 'blank', 'blank'],
        ['blank', 'blank', 'blank'],
        ['blank', 'blank', 'blank']]

screen = pygame.display.set_mode(size)
while True:
    temp = check()
    if (temp[0] != 0):
        pygame.font.init()
        myfont = pygame.font.SysFont('Arial', 25)
        textsurface = myfont.render(temp[1], False, (255, 0, 0))
        screen.blit(textsurface,(0, height))
        textsurface = myfont.render("More?", False, (255, 0, 0))
        screen.blit(textsurface,(300, height))
        textsurface = myfont.render("Over!", False, (255, 0, 0))
        screen.blit(textsurface,(400, height))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if  event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print pos
                if (pos[1] > 600):
                    if (pos[0] >= 300 and pos[0] <= 350):
                        grid = [['blank', 'blank', 'blank'],
                                ['blank', 'blank', 'blank'],
                                ['blank', 'blank', 'blank']]
                    elif (pos[0] >= 400 and pos[0] <= 450):
                        sys.exit()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if  event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print pos
                if (pos[0] < 200):
                    if (pos[1] < 200):
                        if (grid[0][0] == 'blank'):
                            counter += 1
                            if (counter%2 == 0):
                                grid[0][0] = 'cross'
                            else:
                                grid[0][0] = 'naught'
                    elif (pos[1] < 400):
                        if (grid[0][1] == 'blank'):
                            counter += 1
                            if (counter%2 == 0):
                                grid[0][1] = 'cross'
                            else:
                                grid[0][1] = 'naught'
                    elif (pos[1]<600):
                        if (grid[0][2] == 'blank'):
                            counter += 1
                            if (counter%2 == 0):
                                grid[0][2] = 'cross'
                            else:
                                grid[0][2] = 'naught'
                elif (pos[0] < 400):
                    if (pos[1] < 200):
                        if (grid[1][0] == 'blank'):
                            counter += 1
                            if (counter%2 == 0):
                                grid[1][0] = 'cross'
                            else:
                                grid[1][0] = 'naught'
                    elif (pos[1] < 400):
                        if (grid[1][1] == 'blank'):
                            counter += 1
                            if (counter%2 == 0):
                                grid[1][1] = 'cross'
                            else:
                                grid[1][1] = 'naught'
                    elif (pos[1]<600):
                        if (grid[1][2] == 'blank'):
                            counter += 1
                            if (counter%2 == 0):
                                grid[1][2] = 'cross'
                            else:
                                grid[1][2] = 'naught'
                elif (pos[0]<600):
                    if (pos[1] < 200):
                        if (grid[2][0] == 'blank'):
                            counter += 1
                            if (counter%2 == 0):
                                grid[2][0] = 'cross'
                            else:
                                grid[2][0] = 'naught'
                    elif (pos[1] < 400):
                        if (grid[2][1] == 'blank'):
                            counter += 1
                            if (counter%2 == 0):
                                grid[2][1] = 'cross'
                            else:
                                grid[2][1] = 'naught'
                    elif (pos[1]<600):
                        if (grid[2][2] == 'blank'):
                            counter += 1
                            if (counter%2 == 0):
                                grid[2][2] = 'cross'
                            else:
                                grid[2][2] = 'naught'

                print grid[0]
                print grid[1]
                print grid[2]
                print '*****'*5
                        
        screen.fill(white)
        pygame.draw.line(screen, black, [0, height/3], [width, height/3], 2)
        pygame.draw.line(screen, black, [0, 2*height/3], [width, 2*height/3], 2)
        pygame.draw.line(screen, black, [width/3, 0], [width/3, height], 2)
        pygame.draw.line(screen, black, [2*width/3, 0], [2*width/3, height], 2)

        for i in range(3):
            for j in range(3):
                symbol = pygame.image.load(grid[i][j]+'.png')
                symbol_rect = symbol.get_rect()
                symbol_rect.centerx = i*200 + 100
                symbol_rect.centery = j*200 + 100
                screen.blit(symbol, symbol_rect)
                
        pygame.display.flip()

