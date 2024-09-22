# unload_station.py

import simpy

class UnloadStation(object):

    def __init__(self, name, env, speed_factor):
        self.name = name
        self.env = env
        self.speed_factor = speed_factor
        # 5 minutes in hours
        self.unloading_time = 0.083  
        # Only one truck can unload at a time
        self.station = simpy.Resource(env, capacity=1)  

        self.status = dict()
        self.visits = 0
        self.tons = 0
        self.wait_time = 0

    def unload_truck(self, truck):
        with self.station.request() as request:
            print("{} queues at {} at time {}".format(truck.name, self.name, self.env.now))
            yield request  # Wait for station to become available
            print("{} starts unloading at {} at time {}".format(truck.name, self.name, self.env.now))
            yield self.env.timeout(self.unloading_time / self.speed_factor)
            truck.load = 0  # Unload the truck
            print("{} finishes unloading at {} at time {}".format(truck.name, self.name, self.env.now))

    
    def get_wait_time(self):
        # Calculate the total waiting time based on current requests and unloading time
        return len(self.station.queue) * self.unloading_time