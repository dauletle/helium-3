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
    # Add optional argument for the speed factor.
    parser.add_argument('-s', type=float, default=0.00001, help='Speed up the simulation by this factor. (e.g., 10 = 10x real-time)')
    # Add optional argument for the simulation time in hours.
    parser.add_argument('-t', type=int, default=3600, help="Simulation time in hours.  Default is 72 hours.")
    # Add optional argument for enabling the debug flag.
    parser.add_argument('--debug', action='store_true', help="Enable debug mode.")
    args = parser.parse_args()
    return args

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