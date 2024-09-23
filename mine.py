# mine.py

import simpy
import random

import truck
import utils.logger as logger

class Mine:
    def __init__(self, env, debug=False):
        self.debug = debug
        self.env = env
        
    def load_truck(self, truck):
        # Define mining_time to be a random number between 1 and 5 hours, rounded to 2 decimal places
        mining_time = round(random.uniform(1, 5), 2)
        if self.debug: 
            print(f'{truck.name} starts mining at time {self.env.now} for {mining_time:.2f} hours')
        yield self.env.timeout(mining_time)
        # Load the truck at full capacity
        truck.load = truck.capacity
        if self.debug: 
            print("{} finished at time {}".format(truck.name, self.env.now))
