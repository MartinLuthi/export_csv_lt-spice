# Export LTspice Graphs
This script exports graphs from LTspice simulations to .csv format.

# Prerequisites
This code is designed for Debian-based Linux distributions.

# First-time Setup
Make the following scripts executable:
```bash
chmod +x run_lt_spice.sh
chmod +x run_install.sh
```
Run the installation script with sudo:
```bash
sudo ./run_install.sh
```

# Usage
```bash
./run_lt_spice.sh -f f_in.csv -o f_out.csv
```

- -f f_in.csv: Specify the input file (the file with data to be exported).
- -o f_out.csv: Specify the output file (the exported .csv file).