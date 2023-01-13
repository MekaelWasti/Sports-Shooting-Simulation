import pygame
import sys
import simulation

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

    pygame.display.update()


def mouseDrag(e, object, clicked):

    mpx, mpy = pygame.mouse.get_pos()

    if mpx <= object.x + RADIUS and mpx >= object.x - RADIUS and mpy <= object.y + RADIUS and mpy >= object.y - RADIUS:
        hovering = True
    else:
        hovering = False

    if hovering:
        object.color = (154, 154, 154)
    else:
        object.color = (37, 37, 37)

    # x and y of circle is in centerz

    if clicked:
        object.color = (102, 102, 102)
        object.x = mpx
        object.y = mpy
        # print("A ga haj a")

    if e.type == pygame.MOUSEBUTTONDOWN:
        if e.button == 1:
            clicked = True
            if hovering:
                object.color = (154, 154, 154)
                object.x = mpx
                object.y = mpy
                # print("AH")

    if e.type == pygame.MOUSEBUTTONUP:
        if e.button == 1:
            clicked = False
            # print("NAH")

    return clicked


def main():
    run = True
    state = True
    clicked = False

    sim = simulation.SIMULATION()
    ball = simulation.BALL(RADIUS)
    net = simulation.NET()

    while run:
        dt = clock.tick(FPS) * 0.001

        # Simulation input events
        event = pygame.event.poll()
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
                draw_window(ball)

        # Check for MOUSE OBJECT MOVEMENT
        """if mouse is on an object, and is clicked down, it now 'grabs' that object and can
        move it wherever it wants. When let go, if the game is paused the object will stay
        where it's left, if the game is not paused, the physics shall continue as normal
        and the ball will begin to fall"""

        clicked = mouseDrag(event, ball, clicked)

        # Check for point scored
        net.scoreCheck(ball)

        # Controls the speed of this main game loop
        # Will run this game loop at maximum value of FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if state and not clicked:
            ball.move(dt)
            ball.bounce()
            draw_window(ball, net)
        else:
            ball.bounce()
            draw_window(ball, net)

    pygame.quit()


if __name__ == '__main__':
    main()