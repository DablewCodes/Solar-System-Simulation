import itertools
import math
import matplotlib.pyplot as plt
from Vectors import Vector

class CelestialBody:

    min_size = 10
    display_log_base = 1.3

    def __init__(self, solar_system, mass, position = (0,0,0), velocity = (0,0,0), color = "black"):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        self.display_size = max(math.log(self.mass, self.display_log_base), self.min_size)
        self.color = color

        self.solar_system.add_body(self)

    def move(self):
        self.position = (self.position[0] + self.velocity[0],
                         self.position[1] + self.velocity[1],
                         self.position[2] + self.velocity[2])

    def draw(self):
        self.solar_system.ax.plot(
            *self.position,
            marker="o",
            markersize=self.display_size + self.position[0]/28,
            color=self.color)

        if self.solar_system.projection_2d:
            self.solar_system.ax.plot(
                self.position[0],
                self.position[1],
                -self.solar_system.size / 2,
                marker="o",
                markersize=self.display_size / 2,
                color=(.5, .5, .5))

    def gravitational_acceleration(self, other):
        distance = Vector(*other.position) - Vector(*self.position)
        distance_magnitude = distance.get_magnitude()

        force_mag = (self.mass * other.mass) / (distance_magnitude**2)
        force = distance.get_unit_vector() * force_mag

        reverse = 1

        for body in self, other:
            acceleration = force / body.mass
            body.velocity += acceleration*reverse
            reverse = -1

    def check_collision(self, other):

        distance = Vector(*self.position) - Vector(*other.position)
        distance_magnitude = distance.get_magnitude()

        if distance_magnitude < self.display_size/2 + other.display_size/2:
            plt.close()

class Sun(CelestialBody):

    def __init__(self, solar_system, mass=10000, position=(0,0,0),velocity=(0,0,0)):
        super(Sun, self).__init__(solar_system, mass, position, velocity)
        self.color = "yellow"

class Planet(CelestialBody):

    colours = itertools.cycle([(1,0,0),(0,1,0),(0,0,1)])

    def __init__(self, solar_system, mass=10,position=(0,0,0),velocity=(0,0,0)):
        super(Planet, self).__init__(solar_system,mass,position,velocity)
        self.color = next(Planet.colours)