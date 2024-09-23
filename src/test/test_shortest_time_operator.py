import pytest
import sys
import os
import simpy

# Get the directory containing the current script (helium3.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory of `src` to sys.path
# This allows imports to work with the 'src' folder as a package
sys.path.append(os.path.abspath(os.path.join(current_dir, '..')))

from src.mine import Mine 
from src.truck import Truck
from src.utils.tracker import Tracker
from src.operators.shortest_time_operator import ShortestTimeOperator
from src.unload_station import UnloadStation

@pytest.fixture
def env():
    """Fixture to set up a SimPy environment."""
    return simpy.Environment()

@pytest.fixture
def tracker():
    """Fixture to set up a Tracker object."""
    return Tracker()

@pytest.fixture
def unload_stations(env, tracker):
    """Fixture to set up an UnloadStation object."""
    return [UnloadStation("Station_01", env, tracker, debug=False)]

@pytest.fixture
def operator(env, unload_stations):
    """Fixture to set up a ShortestTimeOperator object."""
    return ShortestTimeOperator(env, unload_stations, debug=False)

@pytest.fixture
def mine(env):
    """Fixture to set up a Mine object."""
    return Mine(env, debug=False)

@pytest.fixture
def truck(env, mine, operator, tracker):
    """Create a Truck object for testing."""
    truck = Truck("Truck_01", env, mine, operator, tracker, debug=False)
    yield truck

def test_route_truck(env, mine, operator, tracker, unload_stations, truck):
    """Test if the ShortestTimeOperator routes the truck correctly."""
    # Load the truck
    env.process(mine.load_truck(truck))
    env.process(operator.route_truck(truck))
    env.run(until=100)
    # Check if the truck was able to complete trips.
    station_name = unload_stations[0].name
    assert tracker.station_unloaded_amount[station_name] > 0, "ShortestTimeOperator did not route the truck correctly"