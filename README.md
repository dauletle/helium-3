#

# Helium-3: Python Based Mining Simulator Software
Developed for Vast Take-Home Coding Challenge

Author: Diego Aulet-Leon


## Description
Helium-3 is a Python-based simulation environment built to simulate mining operations.  This project simulates the efficiency of lunar mining trucks transporting Helium-3 between mining sites and unload stations using the SimPy module. The program models real-time processes such as mining, traveling between sites, and unloading resources. The simulation tracks statistics, including truck round trips, wait times, and amounts unloaded. It’s designed to be scalable, customizable, and capable of running faster than real-time to allow for extensive testing and performance analysis.

## Installation
Install the dependencies using the following command in the Command Prompt or Terminal:
```shell
python setup.py install
```
 
Note that this was tested using the following:

### Dependencies and Versions Required for Project:
- pyfiglet==1.0.2
- pytest==8.3.3
- simpy==4.1.1
- typer==0.12.5

### Python Version:
- 3.11.4

### Tested on Operating System:
- macOS Sonoma (Darwin 23.6.0)

## Usage
### Run the simulation
1. Clone the git repository into the desired location.
2. Open the Command Prompt or Terminal, and navigate to the project root folder.
3. Enter the following command to run the simulator.  For instance, this would be how to run the simulation for 
You can run the simulation with the Command Prompt or Terminal.  It is recommended to navigate to the For instance, if a simulation with 75 trucks and 3 unload stations needs to be performed, the following command can be used:
```shell
python run_simulation.py -n 75 -m 3
```

Below is the output for when the -h (help) argument is entered:
```shell
usage: run_simulation.py [-h] -n N -m M [-t T] [--debug]

options:
  -h, --help  show this help message and exit
  -n N        Number of mining trucks.
  -m M        Number of unload stations.
  -t T        Simulation time in hours. Default is 72 hours.
  --debug     Enable debug mode.
```

### Run test scripts
Given that the project has been cloned to the system, and the command prompt or terminal are open in the project root directory, enter the following command to run the test scripts:
```shell
pytest
```

## Challenge Prompt (in PDF file on the repo)
### Objective:
You are tasked with developing a simulation for a lunar Helium-3 space mining operation. This simulation will manage and track the efficiency of mining trucks and unload stations over a continuous 72-hour operation.

### Key Components:
- Mining Trucks: These vehicles perform the actual mining tasks.
- Mining Sites: Locations on the moon where the trucks extract Helium-3. Assume an infinite number of sites, ensuring trucks always have access to mine without waiting.
- Mining Unload Stations: Designated stations where trucks unload the mined Helium-3. Each station can handle one truck at a time.
    
### Operation Details:
- There are (n) mining trucks and (m) mining unload stations.
- Mining trucks can spend a random duration between 1 to 5 hours mining at the sites. 
- It takes a mining truck 30 minutes to travel between a mining site and an unload station. 
	- Assume all trucks are empty at a mining site when the simulation starts.
- Unloading the mined Helium-3 at a station takes 5 minutes.
- Trucks are assigned to the first available unload station. If all stations are occupied, trucks queue at the station with the shortest wait time and remain in their chosen queue.

### Simulation Requirements:
- The simulation must be configurable to accommodate various numbers of mining trucks (n) and unload stations (m). 
- Calculate and report statistics for the performance and efficiency of each mining truck and unload station. 
- The simulation represents 72 hours of non-stop mining and must execute faster than real-time to provide timely analysis.
    
### Language and programming paradigms:  
Please implement this project in Python. Please leverage OOP where it is appropriate.

### Goal of the exercise:
The primary goal of this challenge is to demonstrate your professionalism as a software engineer. This process is designed to mimic a real-world scenario, including design, implementation, and design review. You will be evaluated based on various skills, including:
1. Communication: Clear and concise explanations of your code and design.
2. Documentation: Providing well-documented code and explanations.
3. Code Cleanliness: Writing clean and organized code.
4. Code Deployment: Demonstrating your ability to deploy and manage code.
5. Testing: Implementing appropriate testing strategies.
    

### Things to avoid:
It is not the objective to spend an excessive amount of time on this challenge or create a fully developed system. Feel free to include pseudocode (in comments) to explain what you would do if given more time or resources. The focus is on showcasing your problem-solving and coding skills within a reasonable time frame.

### How to Submit:
Submit your code and any accompanying content, such as data or results, using GitHub or Bitbucket. Please email us a link to your submitted code when you are ready for us to review it.

### Questions:
Please feel free to ask any clarifying questions about this assignment via email with your recruiter.