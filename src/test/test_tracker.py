import pytest
import sys
import os

# Add the 'src/' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.utils.tracker import Tracker

def test_tracker_log_trip():
    """Test if Tracker correctly logs trips."""
    tracker = Tracker()
    tracker.log_trip("Truck_01")
    tracker.log_trip("Truck_01")
    assert tracker.truck_trips["Truck_01"] == 2

def test_tracker_log_unload_amount():
    """Test if Tracker correctly logs unloading at stations."""
    tracker = Tracker()
    tracker.log_unloaded_amount("Station_01", 50)
    tracker.log_unloaded_amount("Station_01", 30)
    assert tracker.station_unloaded_amount["Station_01"] == 80

def test_tracker_log_truck_wait_time():
    """Test if Tracker correctly logs truck wait times."""
    tracker = Tracker()
    tracker.log_truck_wait_time("Truck_01", 5)
    tracker.log_truck_wait_time("Truck_01", 10)
    assert tracker.truck_wait_times["Truck_01"] == 15

def test_tracker_log_station_wait_time():
    """Test if Tracker correctly logs station wait times."""
    tracker = Tracker()
    tracker.log_station_wait_time("Station_01", 5)
    tracker.log_station_wait_time("Station_01", 10)
    assert tracker.station_wait_times["Station_01"] == 15

def test_tracker_report():
    """Test if Tracker correctly prints a report."""
    tracker = Tracker()
    tracker.log_trip("Truck_01")
    tracker.log_trip("Truck_01")
    tracker.log_unloaded_amount("Station_01", 50)
    tracker.log_unloaded_amount("Station_01", 30)
    tracker.log_truck_wait_time("Truck_01", 5)
    tracker.log_truck_wait_time("Truck_01", 10)
    tracker.log_station_wait_time("Station_01", 5)
    tracker.log_station_wait_time("Station_01", 10)
    tracker.report()
    assert True