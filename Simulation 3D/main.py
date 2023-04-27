from SolarSystem import SolarSystem
from CelestialBody import Sun, Planet

def binary_star_simulation():

    #solar_system = SolarSystem(400, projection_2d=True)
    solar_system = SolarSystem(400)

    suns = (Sun(solar_system, position=(40, 120, 40), velocity=(3.5, 0, 3.5)),
            Sun(solar_system, position=(-40, -100, -40), velocity=(-3.5, 0, -3.5)))

    planets = (
        Planet(solar_system, mass=10, position=(100, 200, 0), velocity=(0, 5.5, 5.5)),
        Planet(solar_system, mass=20, position=(-100, -150, -80), velocity=(-7.5, 10, 0)))

    return solar_system

def single_star_simulation():

    #solar_system = SolarSystem(400, projection_2d=True)
    solar_system = SolarSystem(400)

    sun = Sun(solar_system)

    planets = (Planet(solar_system, position=(150, 50, 0),velocity=(0, 5, 5),),
               Planet(solar_system,mass=20,position=(100, -50, 150),velocity=(5, 0, 0)))

    return solar_system

def collision_simulation():

    #solar_system = SolarSystem(400, projection_2d=True)
    solar_system = SolarSystem(400)

    sun = Sun(solar_system)

    planets = (Planet(solar_system, mass=20, position=(150, 50, 0), velocity=(0, 5, 5), ),
               Planet(solar_system, mass=20, position=(175, 50, 0), velocity=(-1, 5, 5)))

    return solar_system

def main():

    solar_system = binary_star_simulation()
    #solar_system = single_star_simulation()
    #solar_system = collision_simulation()

    while 1:
        solar_system.calculate_all_bodies_interactions()
        solar_system.update_all()
        solar_system.draw_all()

if __name__ == '__main__':
    main()