import pygame
import sys
import simulation
import math

# WIDTH, HEIGHT = 900, 500
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation & Modeling | Final Project")
clock = pygame.time.Clock()


fillColor = (25, 25, 25)
WHITE = (255, 255, 255)

FPS = 160  # Target for final
# FPS = 30  # For easier stepping
# ACCELERATION = 9.8
# ACCELERATION = 0.01
# ACCELERATION = 981

# Global Variables
# Params needed for projectile motion
initX = 0
initY = 0
time = 0
power = 0
angle = 0
shoot = False


# Assets - These images are known as "Surfaces"
ICON = pygame.image.load("Assets/taskbarIcon.png")
BASKETBALL = pygame.image.load("Assets/basketball.png")
COURT = pygame.image.load("Assets/court.png")
# HOOP = pygame.image.load("Assets/hoop.png")


# Figma measures coordinates from edge instead of center, need to add RADIUS to match positions
RADIUS = 33

pygame.display.set_icon(ICON)


def draw_window(ball, net):
    '''Draw everything in the window. Responsible for drawing a single frame'''
    WIN.fill(WHITE)

    # Option 1
    # Use WIN.blit() to draw surfaces
    # WIN.blit(BASKETBALL, (WIDTH//2, 450))
    # WIN.blit(COURT, (0, 0))
    # WIN.blit(BASKETBALL, (589, 594))

    # Setup
    # ------------------------------------------------------------------------

    # Ground
    pygame.draw.line(WIN, (70, 70, 70), (0, 717), (1280, 717), 20)

    # Ball
    ball.draw()
    net.draw()
    # Setup
    # ------------------------------------------------------------------------

    mpx, mpy = pygame.mouse.get_pos()
    line = [(ball.x, ball.y), (mpx, mpy)]
    pygame.draw.line(WIN, (0, 0, 0), line[0], line[1])

    pygame.display.update()


def mouseDrag(e, ball, clicked, hovering):
    global shoot, time, initX, initY, power, angle
    initX = ball.x
    initY = ball.y

    mpx, mpy = pygame.mouse.get_pos()

    if mpx <= ball.x + RADIUS and mpx >= ball.x - RADIUS and mpy <= ball.y + RADIUS and mpy >= ball.y - RADIUS:
        hovering = True
    else:
        if not clicked:
            hovering = False

    if hovering:
        ball.color = (154, 154, 154)
    else:
        ball.color = (37, 37, 37)

    # x and y of circle is in centerz

    if clicked and hovering:
        ball.color = (102, 102, 102)
        ball.x = mpx
        ball.y = mpy
        ball.vy = 0
        # print("A ga haj a")

    line = [(ball.x, ball.y), (mpx, mpy)]

    if e.type == pygame.MOUSEBUTTONDOWN:
        if e.button == 1:
            # if hovering:
            #     clicked = True
            #     ball.color = (154, 154, 154)
            #     ball.x = mpx
            #     ball.y = mpy
            #     print("AH")

            if not shoot:
                shoot = True
                # Store initial x and y for projectile motion as it is a function of time
                # We need to keep the x and y the same for the course of the projectile motion
                initX = ball.x
                initY = ball.y
                time = 0
                power = math.sqrt(
                    (line[1][1] - line[0][1])**2 + (line[1][0] - line[0][0])**2)/40
                angle = findAngle((mpx, mpy), ball)
                print(power)
                print(angle)

    # Event is not picking up mousebuttonup if the mouse is moving while the mousebutton is released
    if e.type == pygame.MOUSEBUTTONUP:
        if e.button == 1:
            clicked = False
            print("NAH")
        if not shoot:
            time = 0

    return clicked, hovering, angle


def projectileMotion(initX, initY, power, angle, time):
    print("SHOOOTING")
    vX = math.cos(angle) * power
    vY = math.sin(angle) * power

    distX = vX * time
    distY = (vY * time) + ((-9.8 * (time)**2) / 2)

    nextX = round(distX + initX)
    nextY = round(initY - distY)
    # print(time, time)

    return(nextX, nextY)


def findAngle(pos, ball):
    sX = ball.x
    sY = ball.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle

    return angle


def main():
    global shoot, time, initX, initY, power, angle

    run = True
    state = True
    clicked = False
    hovering = False
    scored = False

    sim = simulation.SIMULATION()
    ball = simulation.BALL(RADIUS)
    net = simulation.NET()

    while run:
        # Controls the speed of this main game loop
        # Will run this game loop at maximum value of FPS
        dt = clock.tick(FPS) * 0.001
        dt = 0.015

        # Simulation input events
        # event = pygame.event.poll()
        # event = pygame.event.get()

        if shoot:
            # if ball.y < 720 - ball.RADIUS - 10:
            if ball.y < 700:
                time += 0.015
                po = projectileMotion(ball.x, ball.y, power, angle, time)
                print("AH")
                print(po)
                ball.x = po[0]
                ball.y = po[1]
            else:
                shoot = False
                # Ground Y
                ball.y = 494
                ball.bounce()

        for event in pygame.event.get():
            # print(event)
            # print("\n\n\n")

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if state and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print("PAUSE")
                sim.pause()
                state = False
                continue
            elif not state and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print("START")
                sim.resume()
                state = True
                continue
            else:
                pass

            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                pygame.quit()
                break

            # step through simulation
            if not state:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    ball.move(dt)
                    draw_window(ball, net)

            if event.type == pygame.QUIT:
                run = False

            # Check for MOUSE OBJECT MOVEMENT
            """if mouse is on an object, and is clicked down, it now 'grabs' that object and can
            move it wherever it wants. When let go, if the game is paused the object will stay
            where it's left, if the game is not paused, the physics shall continue as normal
            and the ball will begin to fall"""

            clicked, hovering, angle = mouseDrag(
                event, ball, clicked, hovering)

        # ----------------------------------------------------------------

        # Check for point scored, with if statement will only update the score if game is in non-paused state
        # if state:
        scored = net.scoreCheck(ball, scored)

        if state and not clicked:
            if not shoot:
                ball.move(dt)
                ball.bounce()
            draw_window(ball, net)
        else:
            ball.bounce()
            draw_window(ball, net)

    pygame.quit()


if __name__ == '__main__':
    main()
