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
        self.records = []

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

    def bounce(self):
        # Call when collision is detected for now with ground
        if self.y > 720 - self.RADIUS - 10:
            self.ACCELERATION = 0
            self.vy = 0
        else:
            self.ACCELERATION = 981

        # def step(self,dt):
        #     '''Step through the simulation by one frame each call'''
        #     self.y += self.vy
        #     self.vy += (self.g * self.dt / self.mass)
        #     self.cur_time += self.dt

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
        self.x2 = 1154
        self.y2 = 411
        self.scoreCount = 0

    def draw(self):
        '''Draw the basketball net object'''

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

        # Score
        pygame.font.init()
        font = pygame.font.Font('Avenir LT Std 65 Medium.otf', 40)
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render(str(self.scoreCount), True, (37, 37, 37))
        WIN.blit(text, (10, 10))

    def scoreCheck(self, ball):
        '''Account for a point scored. Each point for now is 1 point.
        Can account for 2 pointers and 3 pointers later'''

        if ball.x >= self.x1 and ball.x <= self.x2 and ball.y <= self.y1 and ball.y >= self.y2:
            print("SCORE")
            self.scoreCount += 1


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
