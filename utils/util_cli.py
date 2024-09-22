import typer
import pyfiglet
import shutil
import os
import sys
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, required=True, help="Number of mining trucks.")
    parser.add_argument('-m', type=int, required=True, help="Number of unload stations.")
    # Add optional argument for the speed of running the simulation
    parser.add_argument('-s', type=int, default=500, help="Speed factor of running the simulation.  Default is 500.")
    args = parser.parse_args()
    number_of_mining_trucks = args.n
    number_of_unload_stations = args.m
    speed_factor = args.s
    return number_of_mining_trucks, number_of_unload_stations, speed_factor

class TyperCLIApp:
    def __init__(self, app_name:str, function_mappings:dict):
        self.function_mappings = function_mappings
        self.app = typer.Typer()
        self.app_name = app_name

        # Register the start command with Typer
        self.app.command()(self.start)

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def center_text(self, text):
        """Centers the given text based on terminal width."""
        terminal_width = shutil.get_terminal_size().columns
        # Split the text into lines and center each line individually
        centered_lines = [line.center(terminal_width) for line in text.splitlines()]
        return "\n".join(centered_lines)

    def display_logo(self):
        # Display the logo using pyfiglet
        logo = pyfiglet.figlet_format(self.app_name)
        # Center the logo
        typer.echo(self.center_text(logo))
    
    def start(self):
        # Clear screen before displaying the start page
        self.clear_screen()
        self.display_logo()
    
    def exit_app(self):
        """Exit the application."""
        self.clear_screen()  # Clear screen before exiting
        typer.echo(self.center_text("Goodbye!"))
        sys.exit()

    def run(self):
        """Run the Typer application with passed function dictionary."""
        self.start()