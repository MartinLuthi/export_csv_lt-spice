# This script is for Debian-based systems

# Install the dependencies if not already installed
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
. venv/bin/activate

# Install the dependencies
./venv/bin/pip install argparse pandas matplotlib

# Deactivate the virtual environment
deactivate
