# mine.py

import simpy
import random

import truck
import utils.util_logger as util_logger

class Mine:
    def __init__(self, env, speed_factor):
        self.env = env
        self.speed_factor = speed_factor
        
    def load_truck(self, truck):
        # Define mining_time to be a random number between 1 and 5 hours, rounded to 2 decimal places
        mining_time = round(random.uniform(1, 5), 2)
        print(f'{truck.name} starts mining at time {self.env.now} for {mining_time:.2f} hours')
        yield self.env.timeout(mining_time / self.speed_factor)
        # Load the truck at full capacity
        truck.load = truck.capacity
        print("{} finished at time {}".format(truck.name, self.env.now))
