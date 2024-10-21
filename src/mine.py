# mine.py

import simpy
import random
import asyncio

class Mine:
    def __init__(self, speed_factor: float, debug: bool = False):
        """Mine object to simulate the mining process using asyncio."""
        self.speed_factor = speed_factor
        self.debug = debug

    async def load_truck(self, truck):
        """Async simulation of loading materials into the truck."""
        mining_time = round(random.uniform(1, 5), 2)  # Random time between 1 and 5 hours
        if self.debug:
            print(f'{truck.name} starts mining for {mining_time:.2f} hours')
        
        # Convert mining_time to seconds for asyncio.sleep
        await asyncio.sleep((mining_time * 3600) * self.speed_factor)  # Simulate the mining time
        truck.load = truck.capacity  # Load the truck at full capacity
        
        if self.debug:
            print(f'{truck.name} finished mining')

class MineSimPy:
    def __init__(self, env:simpy.Environment, debug:bool=False):
        """Mine object to simulate the mining process. 
        Mines are locations on the moon where the trucks extract Helium-3. 

        Args:
            env (simpy.Environment): Simpy environment to run the simulation.
            debug (bool, optional): Flag to enable debug mode. Defaults to False.
        """
        self.env = env
        self.debug = debug
        
    def load_truck(self, truck):
        """Simulate the mine loading materials into the truck.

        Args:
            truck (Truck): The truck object to load materials into.

        Yields:
            simpy.Event: The event of loading materials into the truck.
        """
        # Define mining_time to be a random number between 1 and 5 hours, rounded to 2 decimal places
        mining_time = round(random.uniform(1, 5), 2)
        if self.debug: 
            print(f'{truck.name} starts mining at time {self.env.now} for {mining_time:.2f} hours')
        yield self.env.timeout(mining_time)
        # Load the truck at full capacity
        truck.load = truck.capacity
        if self.debug: 
            print("{} finished at time {}".format(truck.name, self.env.now))
