##  File: Simulator.py
##  Author: Leo Dahl
## Date: 2025-02-07
##  Uses a grid via Pygame to mark coordinates, marked coordinates are later transferred to the printer to begin the drawing

import pygame
import time
from SerialConnector import RunCommand ## Import SerialConnector

pygame.init()
win = pygame.display.set_mode((300, 300)) # Window size
run = True

Sim = 0
Xmode = True
x, y = 0, 0  # Initial position
vel = 5
Coordinates = []  # Store saved points
Sim = -1
while run:
    pygame.time.delay(30)  # Small delay to smooth movement

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                Xmode = not Xmode
                Sim = Sim+1
                print(Coordinates)  # Debugging output
                Coordinates.append([x, y])  # Store coordinates
                print("Saved coordinates:", x/3, y/3)
            if event.key == pygame.K_RETURN:
                ## Start sending values
                i = 0
                for coord in Coordinates:
                    if coord == Coordinates[0]:
                        ## Move to first point
                        X = coord[0]
                        Y = coord[1]
                        Final = str(X)+","+str(Y)
                        RunCommand(Final,X,Y)
                        i = i + 1
                    else:
                        # Current Coordinates
                        X = coord[0] ## X
                        Y = coord[1] ## Y
                        ## Get X and Y of past coordinate
                        PrevX = Coordinates[i-1][0] 
                        PrevY = Coordinates[i-1][1]
                        ## Get difference between coordinates
                        TotalX = X-PrevX 
                        TotalY = Y-PrevY 
                        Final = str((TotalX)/3)+","+str((TotalY)/3) ## Create string (X,Y)
                        RunCommand(Final) # Run command with values given
                        i = i + 1
                    



            
    # Check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
     if Xmode:
        x -= vel
    if keys[pygame.K_RIGHT]:
     if Xmode:
        x += vel
    if keys[pygame.K_UP]:
     if Xmode == False:
        y -= vel
    if keys[pygame.K_DOWN]:
     if Xmode == False:
        y += vel

    win.fill((0, 0, 0))  # Clear screen before redrawing everything

    # Redraw all saved points
    for coord in Coordinates:
        #print(coord)
        #pygame.draw.rect(win, (0, 255, 0), (coord[v][0], coord[v][1], Coordinates[v][0]-Coordinates[v+1][1], 10))
        pygame.draw.rect(win, (255, 0, 0), (coord[0], coord[1], 10, 10))
     
    # Draw the player at the updated position
    pygame.draw.rect(win, (0, 255, 0), (x, y, 10, 10))

    pygame.display.update()  # Update the display (once per loop)

pygame.quit()
