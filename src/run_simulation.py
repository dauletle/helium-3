import simpy
import sys
import os

# Get the directory containing the current script (helium3.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory of `src` to sys.path
# This allows imports to work with the 'src' folder as a package
sys.path.append(os.path.abspath(os.path.join(current_dir, '..')))

import src.utils.cli as cli
from src.utils.tracker import Tracker
from src.operators.shortest_time_operator import ShortestTimeOperator
from src.unload_station import UnloadStation
from src.truck import Truck
from src.mine import Mine

def __main__():
    # TODO Create interactive CLI.
    args = cli.get_arguments()
    number_of_mining_trucks = args.n
    number_of_unload_stations = args.m
    simulation_time_hours = args.t
    debug = args.debug

    # Initialize SimPy environment
    env = simpy.Environment()

    # Initialize tracker
    tracker = Tracker()

    # Assume infinite mining sites (so no resources needed here)
    mine = Mine(env, debug)
    
    # Create the number of unload_stations.Unloadstation objects specified in number_of_unload_stations
    unload_stations = []
    for i in range(number_of_unload_stations):
        station_name = "UnloadStation{:0{width}}".format(i + 1, width=len(str(number_of_unload_stations)))
        uld_stn = UnloadStation(name=station_name,
                                env=env,
                                tracker=tracker,
                                debug=debug,
                                )
        unload_stations.append(uld_stn)
    
    # Lunar Mine Operator manages routing to unload stations
    # TODO Add option to select operator using the inportlib module.
    lunar_mine_operator = ShortestTimeOperator(env, unload_stations, debug)
    
    # Create the number of mining_trucks.Truck objects specified in number_of_mining_trucks
    mining_trucks = []
    for i in range(number_of_mining_trucks):
        truck_name = "Truck{:0{width}}".format(i + 1, width=len(str(number_of_mining_trucks)))
        trk = Truck(name=truck_name,
                    env=env,
                    mine=mine,
                    operator=lunar_mine_operator,
                    tracker=tracker,
                    debug=debug,
                    )
        mining_trucks.append(trk)
    
    # Run the simulation
    env.run(until=simulation_time_hours)

    # Print the simulation statistics
    # TODO Add option to create datasheets, graphs, etc.
    tracker.report()


if __name__ == "__main__":
    __main__()