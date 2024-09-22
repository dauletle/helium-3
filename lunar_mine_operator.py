# lunar_mine_operator.py

import simpy

class LunarMineOperator:
    def __init__(self, env, unload_stations, speed_factor):
        self.env = env
        self.unload_stations = unload_stations
        self.speed_factor = speed_factor

    def route_truck(self, truck):
        # Initialize variables to store the selected station and the shortest wait time
        shortest_wait_time = float('inf')
        chosen_station = None

        # Iterate over each unload station to find the one with the shortest wait time
        for station in self.unload_stations:
            # Get the wait time for the current station
            current_wait_time = station.get_wait_time()

            # Check if this station has a shorter wait time than the current shortest wait time
            if current_wait_time < shortest_wait_time:
                # If so, update the shortest wait time and set this station as the chosen one
                shortest_wait_time = current_wait_time
                chosen_station = station

        # After checking all stations, route the truck to the station with the shortest wait time
        print("{} is being routed to {} with the shortest wait time at time {}".format(truck.name, chosen_station.name, self.env.now))
        yield self.env.process(chosen_station.unload_truck(truck))