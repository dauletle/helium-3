# Helium-3: Python Based Mining Simulator Software
Developed for Vast Take-Home Coding Challenge

Author: Diego Aulet-Leon

## Description
Helium-3 is a Python-based simulation environment built to simulate mining operations.  This project simulates the efficiency of lunar mining trucks transporting Helium-3 between mining sites and unload stations using the SimPy module. The program models real-time processes such as mining, traveling between sites, and unloading resources. The simulation tracks statistics, including truck round trips, wait times, and amounts unloaded. It’s designed to be scalable, customizable, and capable of running faster than real-time to allow for extensive testing and performance analysis.

## Installation
Before installing the dependencies, setting up a virtual environment to ensure that all dependencies are isolated from the system’s global packages, preventing version conflicts and making the project environment more manageable and portable.  To do this, navigate to the project root directory and create a virtual environment.
```shell
python -m venv venv
```
Then, activate the virtual environment before installing the dependencies.  
- On MacOS or Linux:
```shell
source venv/bin/activate
```
- On Windows:
```shell
.\venv\Scripts\activate
```


Once the virtual environment is setup, install the dependencies using the following command in the Command Prompt or Terminal:
```shell
pip install -r requirements.txt
```

You can confirm the dependencies are installed correctly by running the following command
```shell
pip freeze
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
2. Open the Command Prompt or Terminal and navigate to the project root folder.
3. Activate the Virtual Environment:
- On MacOS or Linux:
```shell
source venv/bin/activate
```
- On Windows:
```shell
.\venv\Scripts\activate
```
4. Enter the following command to run the simulator.  For instance, if a simulation with 75 trucks and 3 unload stations needs to be performed, the following command can be used:
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

When done, you can deactivate the virtual environment by entering:
```shell
deactivate
```
### Design Approach

#### Simulation Using SimPy
The program utilizes SimPy, a discrete-event simulation library, to simulate trucks transporting Helium-3 between lunar mining sites and unload stations. The SimPy module does the following:
- The behavior of active components is modeled with processes. 
- All processes live in an environment. 
- Processes and components interact with the environment and with each other via events. 

Below are the key SimPy concepts applied in the simulation:

##### 1. Environment:
The simulation environment is created using SimPy, and it manages the simulation’s overall flow. The environment handles all time-driven activities, such as mining, traveling, and unloading.

##### 2. Processes:
Each truck in the simulation is modeled as a separate process. These trucks perform several activities in sequence:
- Mining at a lunar site for a random duration. Their lifecycle (mining, traveling, unloading) are modeled using timeouts to simulate real-world delays.
- Traveling from the mining site to the unloading station.
- Waiting for an available unload station and unloading the mined Helium-3.
- Returning to the mining site to start the next cycle.
These activities are modeled using yield env.timeout() to simulate the passage of time between events.

##### 3. Resources:
Unload stations are modeled as shared resources that trucks must request access to. The stations have limited capacity (only one truck at a time can unload at each station). If a station is occupied, a truck waits for the next available station, simulating the queuing and scheduling behavior in real-world systems.

##### 4. Statistics and Tracking:
During the simulation, a custom Tracker class records various statistics like the number of round trips per truck, the amount unloaded at each station and wait times. This helps in evaluating the efficiency of the system after the simulation ends.

### Testing with PyTest
This project uses the PyTest framework to ensure that key components of the simulation are functioning as expected. Unit tests are written for essential modules, such as the Mine, Tracker, and Shortest Time Operator classes. These tests allow for validation of various parts of the simulation, including correct truck movement, accurate resource unloading, and the proper tracking of performance metrics. By leveraging PyTest’s features, the program ensures robust test coverage, providing a foundation for identifying bugs early in the development cycle.

Here are some PyTest concepts applied to the Helium-3 Lunar Mining Simulation project:

##### 1. Fixtures
Fixtures are used in PyTest to provide a fixed baseline resource so that tests can reliably and consistently execute. In the Helium-3 project, fixtures can be applied to create reusable setups, such as initializing the SimPy environment, creating trucks, or setting up mining stations. 

##### 2. Assertions
Assertions are critical for unit testing as they verify whether the output of a function or method matches the expected result, allowing issues to be identified at the function level before integrating the system.  

##### 3. Test Discovery
By placing test files in a test folder with names prefixed by test_ allows PyTest to find and run all test cases without additional configuration, ensuring smooth scalability when new test cases are added.

## Design Considerations for Future Development
The challenge criteria required that when unload stations were not available, trucks should queue at the station with the shortest wait time and remain in their chosen queue. This would be the shortest time algorithm, but there are other approaches that can be more optimal (such as changing the queue when an unload station is available).  

For this reason, extendibility and scalability were the two architectural approaches for this project.  The extendibility attribute was thought out by allowing the operator system to be dynamic for future development of testing different decision-making strategies (along with different unit testing modules).  The scalability attribute was added by accommodating various configurations of trucks and unload stations, with adjustable runtime parameters to speed up or slow down the simulation. This flexibility makes it possible to test different scenarios efficiently using the different command line arguments.

## Conclusion
This project was an enjoyable exercise in demonstrating my approach in building Python-based software. The goal was to show my comfort with researching and applying libraries I hadn’t previously used, like SimPy, ensuring that project objectives were met efficiently. My hope is that my years of experience and education in software development can be evident by demonstrating that my software is simple, clean, and well-organized object-oriented code. The goal for working on this project was to highlight my approaches in testing using PyTest, version control with Git, and deployment through comprehensive and clear documentation.  Please reach out if you have any questions, and I hope that this software demonstrates how well I can contribute to the projects at Vast.  Thank you.

## Challenge Prompt
The prompt is in the PDF file on the repository.