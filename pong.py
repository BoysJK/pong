import sys, pygame, time, random, threading
import player, ball
pygame.init()

# create basic game vars
size = width, height = 320, 240
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grid_size = (11,9)

# create pygame vars
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()



###########################################################
##                        Classes                        ##
###########################################################
players = []
players.append(player.Player("left", screen.get_size()))
players.append(player.Player("right", screen.get_size()))

ball = ball.Ball(screen.get_size())



#############################################################
##                        Game Loop                        ##
#############################################################
key_press = False
while 1:
    # test for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    

    ##########################
    ##      Game logic      ##w
    ##########################
    # 
    screen_size = screen.get_size()

    pygame.event.pump()  # Allow pygame to handle internal actions.
    key = pygame.key.get_pressed()

    # player inputs
    key_press = players[0].key_inputs(key, (pygame.K_w, pygame.K_s), key_press)
    key_press = players[1].key_inputs(key, (pygame.K_UP, pygame.K_DOWN), key_press)
    
    # move players
    for player in players:
        player.move(screen.get_size())
    

    # chnage ball vars if you have pressed a keyw
    if key_press:
        ball.movement = 4
    
        # collision detection
        #for player in players:
            #ball.direction = player.ball_collide(ball.circle[0], ball.direction, screen.get_size())

    # move the ball(s)
    ball.move(screen.get_size())

    ####################
    ##      Draw      ##
    ####################
    # background
    screen.fill(black)

    # draw to screen
    for player in players:
        pygame.draw.rect(screen, white, pygame.Rect(player.rect))
    pygame.draw.circle(screen, white, ball.circle[0], ball.circle[1])
    pygame.draw.polygon(screen, green, players[0].collision_box)
    # pygame.draw.rect(screen, red, ball.debug_square, 1)
    # screen_size = screen.get_size()
    # pygame.draw.rect(screen, red, pygame.Rect(screen_size[0]/2-1, 0, 2, screen_size[1]))
    # pygame.draw.rect(screen, red, pygame.Rect(0 ,screen_size[1]/2-1, screen_size[0], 2))

    # end things
    clock.tick()
    pygame.display.flip()
    time.sleep(.05)