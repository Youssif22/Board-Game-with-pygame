import pygame
##starting the game
pygame.display.init()
white=(255,255,255)
grey=(190,190,190)
red=(255,0,0)
green=(0,255,0)
blue = (0,51,102)
x=233
y=233
r=530
l=530
m=630
k=330
steps = 0
WIDTH = 600
HEIGHT = 600

## the window size and opening
window = pygame.display.set_mode((800,800))
CLOCK = pygame.time.Clock()

#board
def drawboard():
    blocksize = 101
    for x in range(120, WIDTH, blocksize):
        for y in range(130, HEIGHT, blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            pygame.draw.rect(window, white, rect, 1)

##losing situation "the mouse starves to death"
def check(steps):
    if steps==20:
        pygame.draw.rect(window,red, [50, 50, 200, 200])
        pygame.display.update()
        pygame.quit()

## the game starts
while True :
    window.fill(blue)
    drawboard()
    ## draw the mouse and the cat
    mouse = pygame.draw.rect(window, grey, [x, y, 100, 100])
    cat = pygame.draw.rect(window, red, [r, l, 100, 100])
    bridge =pygame.draw.rect(window, green, [m,k, 100, 100])
    pygame.display.update()

    if x == m and y == k:
        pygame.draw.rect(window, green, [50, 50, 200, 200])
        pygame.display.update()
        pygame.quit()
    if x == r and y == l:
        pygame.draw.rect(window, red, [50, 50, 200, 200])
        pygame.display.update()
        pygame.quit()

    ##if mouse == window:
     ##   pygame.draw.rect(window,red, [50, 50, 200, 200])
       ## pygame.display.update()
      ##  pygame.quit()

    ## mouse movements
    for e in pygame.event.get():
        if e.type== pygame.QUIT:
            pygame.quit()
            exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            y-=101
            steps+=1
            check(steps)
        if key[pygame.K_DOWN]:
            y += 101
            steps += 1
            check(steps)
        if key[pygame.K_RIGHT]:
            x+= 101
            steps += 1
            check(steps)
        if key[pygame.K_LEFT]:
            x-= 101
            steps += 1
            check(steps)