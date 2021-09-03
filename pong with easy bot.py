import pygame
import random
import time


#frame rate per second
delay_per_frame = 85

#size of our window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

#size of our paddle
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
#distance from the edge of the window
PADDLE_BUFFER = 10

#size of our ball
BALL_WIDTH = 10
BALL_HEIGHT = 10

#speeds of our paddle and ball
PADDLE_SPEED = 2 #2
BALL_X_SPEED = 3
BALL_Y_SPEED = 2

paddle1YPos = 0
paddle2YPos = 0
ballXDirection = 0
ballYDirection = 0
ballXPos = 0
ballYPos = 0

#RGB colors for our paddle and ball
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#initialize our screen using width and height vars
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

score1 = 0
score2 = 0

#Paddle 1 is our learning agent/us
#paddle 2 is the evil AI

#draw our ball
def drawBall(ballXPos, ballYPos, BALL_WIDTH, BALL_HEIGHT, WHITE):
    #small rectangle, create it
    ball = pygame.Rect(ballXPos, ballYPos, BALL_WIDTH, BALL_HEIGHT)
    #draw it
    pygame.draw.rect(screen, WHITE, ball)


def drawPaddle1(PADDLE_BUFFER, paddle1YPos, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE):
    #crreate it
    paddle1 = pygame.Rect(PADDLE_BUFFER, paddle1YPos, PADDLE_WIDTH, PADDLE_HEIGHT)
    #draw it
    pygame.draw.rect(screen, WHITE, paddle1)


def drawPaddle2(PADDLE_BUFFER, paddle2YPos, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE):
    #create it, opposite side
    paddle2 = pygame.Rect(WINDOW_WIDTH - PADDLE_BUFFER - PADDLE_WIDTH, paddle2YPos, PADDLE_WIDTH, PADDLE_HEIGHT)
    #draw it
    pygame.draw.rect(screen, WHITE, paddle2)


#update the ball, using the paddle posistions the balls positions and the balls directions
def updateBall(score1, score2, paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection):

    #update the x and y position
    ballXPos = ballXPos + ballXDirection * BALL_X_SPEED
    ballYPos = ballYPos + ballYDirection * BALL_Y_SPEED

        #check if hits the other side
    if (
                        ballXPos >= WINDOW_WIDTH - PADDLE_WIDTH - PADDLE_BUFFER and ballYPos + BALL_HEIGHT >= paddle2YPos and ballYPos - BALL_HEIGHT <= paddle2YPos + PADDLE_HEIGHT):
        #switch directions
        ballXDirection = -1
    #past it
    elif (ballXPos >= WINDOW_WIDTH - BALL_WIDTH):
        #positive score
        ballXDirection = -1
        score1 += 1
        paddle1YPos, paddle2YPos, ballXDirection, ballYDirection, ballXPos, ballYPos = new_round(paddle1YPos, paddle2YPos, ballXDirection, ballYDirection, ballXPos, ballYPos)
        time.sleep(0.2)
        return [score1, score2, paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection]
    
    #checks for a collision, if the ball hits the left side, our learning agent
    if (
                        ballXPos <= PADDLE_BUFFER + PADDLE_WIDTH and ballYPos + BALL_HEIGHT >= paddle1YPos and ballYPos - BALL_HEIGHT <= paddle1YPos + PADDLE_HEIGHT):
        #switches directions
        ballXDirection = 1
    #past it
    elif (ballXPos <= 0):
        #negative score
        ballXDirection = 1
        score2 += 1
        paddle1YPos, paddle2YPos, ballXDirection, ballYDirection, ballXPos, ballYPos = new_round(paddle1YPos, paddle2YPos, ballXDirection, ballYDirection, ballXPos, ballYPos)
        time.sleep(0.2)
        return [score1, score2, paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection]
    
    #if it hits the top
    #move down
    if (ballYPos <= 0):
        ballYPos = 0;
        ballYDirection = 1;
    #if it hits the bottom, move up
    elif (ballYPos >= WINDOW_HEIGHT - BALL_HEIGHT):
        ballYPos = WINDOW_HEIGHT - BALL_HEIGHT
        ballYDirection = -1
    return (score1, score2, paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection)

#update the paddle position
def updatePaddle1(paddle1YPos, PADDLE_SPEED):
    paddle1YPos = paddle1YPos + PADDLE_SPEED

    #don't let it move off the screen
    if (paddle1YPos < 0):
        paddle1YPos = 0
    if (paddle1YPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddle1YPos = WINDOW_HEIGHT - PADDLE_HEIGHT
    return paddle1YPos

def updatePaddle2(paddle2YPos, PADDLE_SPEED):
    paddle2YPos -= PADDLE_SPEED
    #don't let it hit top
    if (paddle2YPos < 0):
        paddle2YPos = 0
    #dont let it hit bottom
    if (paddle2YPos > WINDOW_HEIGHT - PADDLE_HEIGHT):
        paddle2YPos = WINDOW_HEIGHT - PADDLE_HEIGHT
    return paddle2YPos

def new_round(paddle1YPos, paddle2YPos, ballXDirection, ballYDirection, ballXPos, ballYPos):
    #random number for initial direction of ball
    num = random.randint(0,9)
    #initialie positions of paddle
    #paddle1YPos = WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2
    #paddle2YPos = WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2
    #and ball direction
    ballXDirection = 1
    ballYDirection = 1
    #starting point
    ballXPos = WINDOW_WIDTH/2 - BALL_WIDTH/2

    #randomly decide where the ball will move
    if(0 < num < 3):
        ballXDirection = 1
        ballYDirection = 1
    if (3 <= num < 5):
        ballXDirection = -1
        ballYDirection = 1
    if (5 <= num < 8):
        ballXDirection = 1
        ballYDirection = -1
    if (8 <= num < 10):
        ballXDirection = -1
        ballYDirection = -1
    #new random number
    num = random.randint(0,9)
    #where it will start, y part
    ballYPos = num*(WINDOW_HEIGHT - BALL_HEIGHT)/9
    return (paddle1YPos, paddle2YPos, ballXDirection, ballYDirection, ballXPos, ballYPos)

# init game
paddle1YPos = WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2
paddle2YPos = WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2
pygame.font.init()
paddle1YPos, paddle2YPos, ballXDirection, ballYDirection, ballXPos, ballYPos = new_round(paddle1YPos, paddle2YPos, ballXDirection, ballYDirection, ballXPos, ballYPos)
drawBall(ballXPos, ballYPos, BALL_WIDTH, BALL_HEIGHT, WHITE)
drawPaddle1(PADDLE_BUFFER, paddle1YPos, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)
drawPaddle2(PADDLE_BUFFER, paddle2YPos, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)

while True:

    if ballYPos > paddle1YPos + PADDLE_HEIGHT/2:
        if ballXPos > WINDOW_WIDTH/2 and paddle1YPos+PADDLE_HEIGHT/2 < WINDOW_HEIGHT-50 and paddle1YPos+PADDLE_HEIGHT/2 > WINDOW_HEIGHT-60:
            pass
        else:
            paddle1YPos = updatePaddle1(paddle1YPos, PADDLE_SPEED)
    elif ballYPos < paddle1YPos + PADDLE_HEIGHT/2:
        if ballXPos > WINDOW_WIDTH/2 and paddle1YPos+PADDLE_HEIGHT/2 < 50 and paddle1YPos+PADDLE_HEIGHT/2 > 60:
            pass
        else:
            paddle1YPos = updatePaddle1(paddle1YPos, -PADDLE_SPEED)
    drawPaddle1(PADDLE_BUFFER, paddle1YPos, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)

    #print("YPos1: ", paddle1YPos)
    #print("Ball: ", ballXPos, ballYPos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
                paddle2YPos = updatePaddle2(paddle2YPos, PADDLE_SPEED)
                drawPaddle1(PADDLE_BUFFER, paddle2YPos, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)
    elif keys[pygame.K_DOWN]:
                paddle2YPos = updatePaddle2(paddle2YPos, -PADDLE_SPEED)
                drawPaddle1(PADDLE_BUFFER, paddle2YPos, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)

    pygame.event.pump()
    
    screen.fill(BLACK)
    drawPaddle1(PADDLE_BUFFER, paddle1YPos, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)
    drawPaddle2(PADDLE_BUFFER, paddle2YPos, PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)
    drawBall(ballXPos, ballYPos, BALL_WIDTH, BALL_HEIGHT, WHITE)
    score1, score2, paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection = updateBall(score1, score2, paddle1YPos, paddle2YPos, ballXPos, ballYPos, ballXDirection, ballYDirection)

    text = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = text.render(f'{score1}          {score2}', False, (50, 50, 50))
    text_rect = textsurface.get_rect(center=(WINDOW_WIDTH/2, 70))
    screen.blit(textsurface,text_rect)

    time.sleep(1/delay_per_frame)
    pygame.display.flip()
