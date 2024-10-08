import argparse
import pandas as pd
import matplotlib.pyplot as plt
import re

# parse_txt_file: str -> DataFrame
def parse_txt_file(file_path):
    time = []
    signals = {}
    
    with open(file_path, 'r', encoding='latin-1') as file:
        header = next(file)  # Skip the header line
        signal_names = header.split()[1:]  # Get the signal names from the header
        
        for line in file:
            parts = line.split()
            time_val = float(parts[0])
            time.append(time_val)

            # Iterate over signal columns
            for i, signal in enumerate(parts[1:], 1):
                # Check if the signal contains parentheses (complex signal like dB and phase)
                if '(' in signal and ')' in signal:
                    matches = re.findall(r'\(([^)]+)\)', signal)
                    if matches:
                        magnitude_phase = matches[0].split(',')
                        magnitude = float(magnitude_phase[0].replace('dB', ''))
                        phase = float(magnitude_phase[1].replace('°', ''))

                        if f'{signal_names[i-1]} Magnitude' not in signals:
                            signals[f'{signal_names[i-1]} Magnitude'] = []
                        if f'{signal_names[i-1]} Phase' not in signals:
                            signals[f'{signal_names[i-1]} Phase'] = []

                        signals[f'{signal_names[i-1]} Magnitude'].append(magnitude)
                        signals[f'{signal_names[i-1]} Phase'].append(phase)
                else:
                    # Simple signal without parentheses (e.g., voltage)
                    value = float(signal)
                    if signal_names[i-1] not in signals:
                        signals[signal_names[i-1]] = []
                    signals[signal_names[i-1]].append(value)

    data = {'Time': time}
    # Flatten the signals dictionary into columns
    for signal, values in signals.items():
        data[signal] = values

    return pd.DataFrame(data)

# write_csv_file with DataFrame
def write_csv_file(output_path, data):
    data.to_csv(output_path, index=False)

# plot_data with DataFrame
def plot_data(data):
    fig, ax = plt.subplots()
    ax.set_xlabel('Time / Frequency')

    # Plot each signal trace
    for column in data.columns[1:]:
        ax.plot(data['Time'], data[column], label=column)

    ax.legend()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Process LTspice .txt file and convert to .csv')
    parser.add_argument('-f', '--file', required=True, help='Input .txt file')
    parser.add_argument('-o', '--output', required=True, help='Output .csv file')
    args = parser.parse_args()

    data = parse_txt_file(args.file)
    write_csv_file(args.output, data)
    plot_data(data)

if __name__ == "__main__":
    main()
