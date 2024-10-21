import simpy
import sys
import os
import asyncio

# Get the directory containing the current script (helium3.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory of `src` to sys.path
# This allows imports to work with the 'src' folder as a package
sys.path.append(os.path.abspath(os.path.join(current_dir, '..')))

import src.utils.cli as cli
from src.utils.tracker import Tracker
from src.operators.shortest_time_operator import ShortestTimeOperatorSimPy, ShortestTimeOperator
from src.unload_station import UnloadStationSimPy, UnloadStation
from src.truck import TruckSimPy, Truck
from src.mine import MineSimPy, Mine

async def run_simulation(args):
    # TODO Create interactive CLI.
    number_of_mining_trucks = args.n
    number_of_unload_stations = args.m
    simulation_time_hours = args.t
    speed_factor = args.s
    debug = args.debug

    # Convert simulation time to seconds (since we're tracking real-world time)
    simulation_time_seconds = simulation_time_hours * 3600

    # Initialize SimPy environment
    # env = simpy.Environment()

    # Initialize tracker
    tracker = Tracker()

    # Assume infinite mining sites (so no resources needed here)
    mine = Mine(speed_factor=speed_factor, 
                debug=debug)
    
    # Create the number of unload_stations.Unloadstation objects specified in number_of_unload_stations
    unload_stations = []
    for i in range(number_of_unload_stations):
        station_name = "UnloadStation{:0{width}}".format(i + 1, width=len(str(number_of_unload_stations)))
        uld_stn = UnloadStation(name=station_name, 
                                       speed_factor=speed_factor,
                                       tracker=tracker, 
                                       debug=debug)
        unload_stations.append(uld_stn)
    
    # Lunar Mine Operator manages routing to unload stations
    # TODO Add option to select operator using the inportlib module.
    lunar_mine_operator = ShortestTimeOperator(unload_stations=unload_stations, 
                                               speed_factor=speed_factor,
                                               debug=debug)

    # Create the number of mining_trucks.Truck objects specified in number_of_mining_trucks
    mining_trucks = []
    for i in range(number_of_mining_trucks):
        truck_name = "Truck{:0{width}}".format(i + 1, width=len(str(number_of_mining_trucks)))
        trk = Truck(name=truck_name, 
                      mine=mine, 
                      operator=lunar_mine_operator,
                      speed_factor=speed_factor, 
                      tracker=tracker, 
                      debug=debug)
        mining_trucks.append(trk)

    # Schedule the trucks to run the simulation
    truck_tasks = [truck.work() for truck in mining_trucks]

     # Start event loop time tracking
    loop = asyncio.get_event_loop()
    start_time = loop.time()  # Get event loop time in seconds
    simulation_time_seconds = simulation_time_hours * 3600

    # Function to check if the simulation should stop
    async def check_time():
        while True:
            current_time = loop.time()
            elapsed_time = (current_time - start_time)  # In seconds
            elapsed_time_hours = elapsed_time / 3600  # Convert to hours
            if elapsed_time >= simulation_time_seconds:
                print(f"Simulation stopped after {elapsed_time_hours:.2f} hours (scaled by speed factor: {speed_factor})")
                break
            await asyncio.sleep(1)  # Check every second

    # Run the simulation and time check concurrently
    time_checker = asyncio.create_task(check_time())
    await asyncio.gather(*truck_tasks, time_checker)


    # Print the simulation statistics
    # TODO Add option to create datasheets, graphs, etc.
    tracker.report()


def __main__():
    """Main function needs to set up and run the simulation."""
    # Parse command-line arguments using CLI
    args = cli.get_arguments()

    # Run the simulation asynchronously
    asyncio.run(run_simulation(args))


if __name__ == "__main__":
    __main__()