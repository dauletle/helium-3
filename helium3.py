import simpy

import utils.cli as cli
from utils.tracker import Tracker
from operators.lunar_mine_operator import LunarMineOperator
from unload_station import UnloadStation
from truck import Truck
from mine import Mine

def __main__():
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
    lunar_mine_operator = LunarMineOperator(env, unload_stations, debug)
    
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
    tracker.report()


if __name__ == "__main__":
    __main__()