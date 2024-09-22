# trucks.py
import simpy

class Truck:
    def __init__(self, name, env, mine, operator, speed_factor):
        self.name = name
        self.env = env
        self.mine = mine
        self.operator = operator
        self.capacity = 100
        self.travel_time = 0.5
        # The truck starts with no load
        self.load = 0
        self.speed_factor = speed_factor
        self.action = env.process(self.work())

    def work(self):
        while True:
            # Go to the mine and load the truck
            yield self.env.process(self.mine.load_truck(self))

            # Travel to the unload station (30 minutes travel time)
            print("{} is traveling to unload station at time {}".format(self.name, self.env.now))
            yield self.env.timeout(self.travel_time / self.speed_factor)

            # Unload at the unload station (operator routes to an available station)
            yield self.env.process(self.operator.route_truck(self))

            # Travel back to the mine (30 minutes travel time)
            print("{} is done at time {}".format(self.name, self.env.now))
            yield self.env.timeout(self.travel_time / self.speed_factor)
