import sys
import pygame


pygame.init()
screen = pygame.display.set_mode((500, 500))


class Ball:

    # Pass the xv, yv as arguments as well.
    def __init__(self, x=20, y=400, xv=0, yv=0, color=(0, 0, 0)):
        self.x = x
        self.y = y
        # Give the objects xv and yv attributes.
        self.xv = xv
        self.yv = yv
        self.position = (self.x, self.y)
        self.visible = False

    def draw(self, s):
        if self.visible == True:
            pygame.draw.circle(s, (255, 0, 0), (int(self.x), int(self.y)), 8)

    def get_rect(self):
        pass

    def getLoc(self):
        return (self.x, self.y)

    def setLoc(self, x, y):
        self.x = x
        self.y = y

    def moveX(self, dt):
        self.x += dt * self.xv

    def moveY(self, dt):
        self.y += dt * self.yv

    # Add a method to update the position and other attributes.
    # Call it every frame.
    def update(self, dt):
        self.moveX(dt)
        self.moveY(dt)

        if self.y > 400:
            self.yv = -R * self.yv
            self.xv = eta * self.xv
        else:
            self.yv = self.yv - g * dt


dt = 0.1
g = 6.67
R = 0.7
eta = 0.5

balls = []
clock = pygame.time.Clock()
rel_x = 0
rel_y = 0

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or
                event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            # Create a new ball instance and append it to the list.
            # Pass the rel (the relative mouse movement) as well.
            # * 10 to make the balls faster.
            ball = Ball(xv=rel_x*10, yv=rel_y*10)
            ball.visible = True
            balls.append(ball)
        if event.type == pygame.MOUSEMOTION:
            # event.rel is the relative movement of the mouse.
            rel_x = event.rel[0]
            rel_y = event.rel[1]

    # Call the update methods of all balls.
    for ball in balls:
        ball.update(dt)

    # Clear the screen with fill (or blit a background surface).
    screen.fill((255, 255, 255))
    # Draw the balls.
    for ball in balls:
        ball.draw(screen)

    pygame.display.update()
    dt = clock.tick(160) / 1000
