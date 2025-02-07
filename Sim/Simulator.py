import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
run = True

Sim = 0
Xmode = True
x, y = 250, 250  # Initial position
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
                print("Saved coordinates:", x, y)
            if event.key == pygame.K_RETURN:
                ## Start sending values
                i = 0
                for coord in Coordinates:
                    if coord == Coordinates[0]:
                        ## Move to first point
                        X = coord[0]
                        Y = coord[1]
                        output = str(x) + ",", str(y)
                        print(output)
                        i = i + 1
                    else:
                        X = coord[0]
                        Y = coord[1]
                        PrevX = Coordinates[i-1][0]
                        PrevY = Coordinates[i-1][1]
                        print("Scanning")
                        print(i)
                        i = i + 1
                        print("To move from pos" + str(i-1) + "to pos" + str(i))
                        print("X: ", X-PrevX)
                        print("Y: ", Y-PrevY)

                    



            
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
