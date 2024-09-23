# unload_station.py

import simpy

class UnloadStation(object):

    def __init__(self, name, env, tracker, debug=False):
        self.name = name
        self.env = env
        # 5 minutes in hours
        self.unloading_time = 0.083  
        # Only one truck can unload at a time
        self.station = simpy.Resource(env, capacity=1)  
        self.tracker = tracker
        self.debug = debug

        self.status = dict()
        self.visits = 0
        self.tons = 0
        self.wait_time = 0

    def unload_truck(self, truck):
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
        # Calculate the total waiting time based on current requests and unloading time
        return len(self.station.queue) * self.unloading_time