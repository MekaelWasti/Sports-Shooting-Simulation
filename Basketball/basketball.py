import pygame
import time

# WIDTH, HEIGHT = 900, 500
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation & Modeling | Final Project")

fillColor = (25, 25, 25)
fillColor = (255, 255, 255)

FPS = 160
previousTime = time.time()
ACCELERATION = -9.8
ACCELERATION = 0.5


class Ball():
    def __init__(self, RADIUS):
        self.RADIUS = RADIUS
        self.x = 99 + RADIUS
        self.y = 646 + RADIUS
        self.y = 40
        self.velocity = 0

    def draw(self):
        pygame.draw.circle(WIN, (37, 37, 37),
                           (self.x, self.y), self.RADIUS)

    def move(self):
        self.velocity += ACCELERATION
        self.y += self.velocity


# Assets - These images are known as "Surfaces"
ICON = pygame.image.load("Assets/taskbarIcon.png")
BASKETBALL = pygame.image.load("Assets/basketball.png")
COURT = pygame.image.load("Assets/court.png")
# HOOP = pygame.image.load("Assets/hoop.png")


# Figma measures coordinates from edge instead of center, need to add RADIUS to match positions
RADIUS = 33

pygame.display.set_icon(ICON)


def draw_window(ball):
    WIN.fill(fillColor)

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

    # Net

    # Pole
    pygame.draw.line(WIN, (0, 0, 0), (1154, 715), (1154, 411), 20)
    # Backboard
    POLEWIDTH = 18 + 4
    RIMWIDTH = 21
    pygame.draw.line(WIN, (183, 183, 183), (1172 - POLEWIDTH,
                     313), (1172 - POLEWIDTH, 411), 28)
    # Rim
    pygame.draw.line(WIN, (183, 183, 183), (1046, 411 - RIMWIDTH//2),
                     (1154, 411 - RIMWIDTH//2), RIMWIDTH)
    # Setup
    # ------------------------------------------------------------------------

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True

    ball = Ball(RADIUS)

    while run:
        # Controls the speed of this main game loop
        # Will run this game loop at maximum value of FPS
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        ball.move()

        draw_window(ball)

    pygame.quit()


if __name__ == '__main__':
    main()
