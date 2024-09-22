import simpy

import utils.util_cli as util_cli
from unload_station import UnloadStation
from truck import Truck
from mine import Mine
from lunar_mine_operator import LunarMineOperator

SIMULATION_TIME_HOURS = 72 * 60

def __main__():
    number_of_mining_trucks, number_of_unload_stations, speed_factor = util_cli.get_arguments()

    # Initialize SimPy environment
    env = simpy.Environment()

    # Assume infinite mining sites (so no resources needed here)
    mine = Mine(env, speed_factor)
    
    # Create the number of unload_stations.Unloadstation objects specified in number_of_unload_stations
    unload_stations = []
    for i in range(number_of_unload_stations):
        uld_stn = UnloadStation(name="UnloadStation{}".format(i + 1),
                                env=env,
                                speed_factor=speed_factor)
        unload_stations.append(uld_stn)
    
    # Lunar Mine Operator manages routing to unload stations
    lunar_mine_operator = LunarMineOperator(env, 
                                            unload_stations,
                                            speed_factor)
    
    # Create the number of mining_trucks.Truck objects specified in number_of_mining_trucks
    mining_trucks = []
    for i in range(number_of_mining_trucks):
        trk = Truck(name="Truck{}".format(i + 1),
                    env=env,
                    mine=mine,
                    operator=lunar_mine_operator,
                    speed_factor=speed_factor)
        mining_trucks.append(trk)
    
    # Run the simulation
    env.run(until=SIMULATION_TIME_HOURS/speed_factor)


if __name__ == "__main__":
    __main__()