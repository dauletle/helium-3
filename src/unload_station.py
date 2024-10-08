# unload_station.py

import simpy

from src.utils.tracker import Tracker
from src.truck import Truck

class UnloadStation(object):

    def __init__(self, name:str, env:simpy.Environment, tracker:Tracker, debug=False):
        """Unload Station object to simulate the unload station. 
        Unload stations are designated stations where trucks unload the mined Helium-3. 
        Assume: 
        - Each station can handle one truck at a time.
        - Unloading takes 5 minutes.

        Args:
            name (str): Name of the unload station.
            env (simpy.Environment): Simpy environment to run the simulation.
            tracker (Tracker): Tracker object to track statistics of the simulation.
            debug (bool, optional): Flag to enable debug mode. Defaults to False.
        """
        self.name = name
        self.env = env
        # 5 minutes in hours
        self.unloading_time = 0.083  
        # Only one truck can unload at a time
        self.station = simpy.Resource(env, capacity=1)  
        self.tracker = tracker
        self.debug = debug

        self.status = dict()
        self.wait_time = 0

    def unload_truck(self, truck:Truck):
        """Simulate the unload station unloading the truck.

        Args:
            truck (Truck): The truck object to unload.

        Yields:
            simpy.Event: The event of unloading the truck.
        """
        with self.station.request() as request:
            start_wait = self.env.now
            if self.debug: 
                print("{} queues at {} at time {}".format(truck.name, self.name, start_wait))
            yield request  # Wait for station to become available
            wait_time = self.env.now - start_wait
            self.tracker.log_truck_wait_time(truck.name, wait_time)
            self.tracker.log_station_wait_time(self.name, wait_time)

            if self.debug: 
                print("{} starts unloading at {} at time {}".format(truck.name, self.name, self.env.now))
            yield self.env.timeout(self.unloading_time)
            self.tracker.log_unloaded_amount(self.name, truck.load)
            truck.load = 0  # Unload the truck
            if self.debug: 
                print("{} finishes unloading at {} at time {}".format(truck.name, self.name, self.env.now))

    
    def get_wait_time(self):
        """Calculate the total waiting time based on current requests and unloading time.

        Returns:
            int: The total waiting time.
        """
        return len(self.station.queue) * self.unloading_time