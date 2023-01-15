import pygame
from main import WIN


class BALL():
    '''Basketball Object'''

    def __init__(self, RADIUS):
        self.RADIUS = RADIUS
        self.x = 99 + RADIUS
        self.y = 646 + RADIUS
        self.y = 40
        self.mass = 60
        '''Mass of a basketball is 60kg'''
        self.vy = 0
        self.gravity = .35
        self.bounceEnergyLoss = -.12
        self.friction = -.12
        self.color = (37, 37, 37)
        self.ACCELERATION = 981
        self.time = 0
        self.power = 0
        self.angle = 0

    def draw(self):
        '''Draw the ball object in it's respective coordinates'''
        pygame.draw.circle(WIN, self.color,
                           (self.x, self.y), self.RADIUS)

    def move(self, dt):
        '''Make the Ball object move in accordance to the vy, acceleration and friction with delta time taken into account'''
        self.vy += self.ACCELERATION * dt
        self.y += self.vy * dt
        # print(f'Velocity: {self.vy}')
        # print(f'\nY POSITION: {self.y}')

    def limitvy(self, maxvy):
        min(-maxvy, max(self.vy.x))

    def bounce(self, dt):
        # Call when collision is detected for now with ground
        if self.y > 720 - self.RADIUS - 10:
            # if self.y > 720:
            # print("AH")
            # print(self.vy)
            # self.ACCELERATION = 0
            # self.ACCELERATION = -981 * dt
            # print(self.vy)
            self.ACCELERATION = -981
            # self.vy = 0
            self.y = 720 - self.RADIUS - 10
            # Attempt to add energy loss by percentage ballpark of 20% loss per bounce
            self.vy = self.vy*-0.8 * dt*100
            # self.vy = int(self.vy)*-0.8 * dt * 100
        else:
            self.ACCELERATION = 981
        if self.x > 1280 - self.RADIUS:
            # Temporary bound checking for right
            self.ACCELERATION = 0
            self.vy = 0
            self.x = 1280 - self.RADIUS
        if self.x < 0 + self.RADIUS:
            # Temporary bound checking for right
            self.ACCELERATION = 0
            self.vy = 0
            self.x = 0 + self.RADIUS

        def step(self, dt):
            '''Step through the simulation by one frame each call'''
            self.y += self.vy
            self.vy += (self.g * self.dt / self.mass)
            self.cur_time += self.dt

    def pause(self):
        '''Pause the ball's movements'''

    def resume(self):
        '''Resume the ball's movements'''


class NET():
    '''Net Object'''

    def __init__(self):
        # Only need the coordinates of the actual rim to
        # check for scoring
        self.x1 = 1046
        self.y1 = 411
        '''Y coordinate representing the bottom of the rim'''
        self.x2 = 1154
        self.y2 = 411 - 22
        '''Y coordinate representing the top of the rim'''
        self.scoreCount = 0

    def draw(self):
        '''Draw the basketball net object'''

        # Pole
        pygame.draw.line(WIN, (0, 0, 0), (1154, 715), (1154, self.y1), 20)

        # Backboard
        POLEWIDTH = 18 + 4
        RIMWIDTH = 21
        pygame.draw.line(WIN, (183, 183, 183), (1172 - POLEWIDTH,
                                                313), (1172 - POLEWIDTH, self.y1), 28)

        # Rim
        pygame.draw.line(WIN, (183, 183, 183), (self.x1, self.y1 - RIMWIDTH//2),
                         (1154, self.y1 - RIMWIDTH//2), RIMWIDTH)

        # Score
        pygame.font.init()
        font = pygame.font.Font('Avenir LT Std 65 Medium.otf', 40)
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render(str(self.scoreCount), True, (37, 37, 37))
        WIN.blit(text, (10, 10))

    def scoreCheck(self, ball, scored):
        '''Account for a point scored. Each point for now is 1 point.
        Can account for 2 pointers and 3 pointers later'''

        if ball.x >= self.x1 and ball.x <= self.x2 and ball.y >= self.y2 and ball.y <= self.y1:
            scored = True
            print("SCORE")
            self.scoreCount += 1
        return scored


class SIMULATION():

    def __init__(self):
        # Delta time
        # self.dt = dt
        self.paused = False
        '''Simulation is unpaused by default'''

    def pause(self):
        '''Pause the simulation'''
        self.paused = True

    def resume(self):
        '''Resume the simulation'''
        self.paused = False
