# trucks.py
import simpy

from src.mine import Mine
from src.operators.shortest_time_operator import ShortestTimeOperator
from src.utils.tracker import Tracker

class Truck:
    def __init__(self, name:str, env:simpy.Environment, mine:Mine, operator:ShortestTimeOperator, tracker:Tracker, debug:bool=False):
        self.name = name
        self.env = env
        self.mine = mine
        self.operator = operator
        self.capacity = 100
        self.travel_time = 0.5
        # The truck starts with no load
        self.load = 0
        self.tracker = tracker
        self.debug = debug
        self.action = env.process(self.work())

    def work(self):
        """Simulation of the truck loading materials, traveling to a unload station, unloading materials, then returning to the mine.

        Yields:
            simpy.Event: The event of the truck working.
        """
        while True:
            # Go to the mine and load the truck
            yield self.env.process(self.mine.load_truck(self))

            # Travel to the unload station (30 minutes travel time)
            if self.debug: 
                print("{} is traveling to unload station at time {}".format(self.name, self.env.now))
            yield self.env.timeout(self.travel_time)

            # Unload at the unload station (operator routes to an available station)
            yield self.env.process(self.operator.route_truck(self))

            # Travel back to the mine (30 minutes travel time)
            if self.debug: 
                print("{} is done at time {}".format(self.name, self.env.now))
            yield self.env.timeout(self.travel_time)

            # Log the roundtrip here, after returning to the mine
            self.tracker.log_trip(self.name)
