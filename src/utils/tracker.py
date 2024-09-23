# tracker.py

class Tracker:
    def __init__(self):
        self.truck_trips = {}
        self.station_unloaded_amount = {}
        self.truck_wait_times = {}
        self.station_wait_times = {}

    def log_trip(self, truck_name):
        """Log each roundtrip for the truck."""
        if truck_name not in self.truck_trips:
            self.truck_trips[truck_name] = 0
        self.truck_trips[truck_name] += 1

    def log_unloaded_amount(self, station_name, amount):
        """Log the amount unloaded at each station."""
        if station_name not in self.station_unloaded_amount:
            self.station_unloaded_amount[station_name] = 0
        self.station_unloaded_amount[station_name] += amount

    def log_truck_wait_time(self, truck_name, wait_time):
        """Log the total wait time for each truck."""
        if truck_name not in self.truck_wait_times:
            self.truck_wait_times[truck_name] = 0
        self.truck_wait_times[truck_name] += wait_time

    def log_station_wait_time(self, station_name, wait_time):
        """Log the total wait time for each unload station."""
        if station_name not in self.station_wait_times:
            self.station_wait_times[station_name] = 0
        self.station_wait_times[station_name] += wait_time

    def report(self):
        """Print a summary of all collected statistics in sorted order."""
        print("\nSimulation Statistics Summary:")

        # Sort and print number of trips per truck (sorted by truck name)
        # print("\nNumber of trips per truck:")
        # for truck, trips in sorted(self.truck_trips.items()):
        #     print(f"{truck}: {trips} trips")
        
        # Print average number of truck trips, as well as the maximum number of trips, and the minimum number of trips
        print(f"\nAverage number of trips per truck: {sum(self.truck_trips.values()) / len(self.truck_trips)}")
        print(f"Maximum number of trips: {max(self.truck_trips.values())}")
        print(f"Minimum number of trips: {min(self.truck_trips.values())}")

        # Sort and print amount unloaded at each station (sorted by station name)
        print("\nAmount unloaded at each station:")
        for station, amount in sorted(self.station_unloaded_amount.items()):
            print(f"{station}: {amount} units of Helium-3")

        # Sort and print total wait time per truck (sorted by truck name)
        # print("\nTotal wait time per truck (hours):")
        # for truck, wait_time in sorted(self.truck_wait_times.items()):
        #     print(f"{truck}: {wait_time:.2f} hours")
        
        # Print average truck wait time, as well as the maximum truck wait time, and the minimum truck wait time
        average = round(sum(self.truck_wait_times.values()) / len(self.truck_wait_times), 5)
        print(f"\nAverage truck wait time: {average:.2f} hours")
        print(f"Maximum truck wait time: {max(self.truck_wait_times.values()):.2f} hours")
        print(f"Minimum truck wait time: {min(self.truck_wait_times.values()):.2f} hours")

        # Sort and print total wait time per unload station (sorted by station name)
        print("\nTotal wait time per unload station (hours):")
        for station, wait_time in sorted(self.station_wait_times.items()):
            print(f"{station}: {wait_time:.2f} hours")