import setuptools
import os
import pkg_resources
import subprocess
import sys

# Read the requirements from the requirements.txt file
def get_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

# Check if a specific package is installed and matches the required version
def check_installed_versions(requirements):
    for requirement in requirements:
        pkg_name, pkg_version = None, None

        # Split package name and version
        if '==' in requirement:
            pkg_name, pkg_version = requirement.split('==')
        else:
            pkg_name = requirement

        try:
            # Check if the package is installed
            installed_pkg = pkg_resources.get_distribution(pkg_name)
            installed_version = installed_pkg.version

            if pkg_version and installed_version != pkg_version:
                # Mismatch found, prompt the user
                print(f"\n{pkg_name} is installed with version {installed_version}. "
                      f"The required version is {pkg_version}.")

                # Ask user for confirmation to install the required version
                confirmation = input(f"Do you want to install {pkg_name} {pkg_version}? (y/n): ").lower()
                if confirmation == 'y':
                    install_package(f"{pkg_name}=={pkg_version}")
                else:
                    print(f"Keeping the installed version of {pkg_name}.")
            else:
                print(f"{pkg_name} is already installed with the correct version {installed_version}.")
        except pkg_resources.DistributionNotFound:
            print(f"{pkg_name} is not installed. Installing now...")
            install_package(requirement)

# Install the package using pip
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Main setup function
def main():
    requirements = get_requirements()
    check_installed_versions(requirements)

    setuptools.setup(
        name="helium3_simulation",
        version="0.1.0",
        author="Diego Aulet-Leon",
        author_email="dauletle@egmail.com",
        description="A Python-based simulation environment built to simulate mining operations.",
        packages=setuptools.find_packages(),
        install_requires=requirements,  # Install required dependencies
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.7',  # Specify Python version requirement if necessary
    )

if __name__ == "__main__":
    main()