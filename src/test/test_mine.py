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
def mine(env):
    """Fixture to set up a Mine object."""
    return Mine(env, debug=False)

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
def truck(env, mine, operator, tracker):
    """Create a Truck object for testing."""
    truck = Truck("Truck_01", env, mine, operator, tracker, debug=False)
    yield truck

def test_mine_creation(mine):
    """Test that a Mine object is created successfully."""
    assert isinstance(mine, Mine), "Mine object was not created successfully"

def test_mine_loading(mine, truck, env):
    """Test that the Mine object loads materials correctly."""
    # Create a Truck object
    env.process(mine.load_truck(truck))
    env.run(until=100)
    assert truck.load == 100, "Truck did not load materials correctly"

# Add additional tests to check edge cases, performance, etc.

if __name__ == "__main__":
    pytest.main()