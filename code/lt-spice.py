# Trait le .txt généré par LTspice et le convertit en .csv utilisable
# Produit également un graphique
# le programme doit être lancé avec la commande suivante:
# python lt-spice.py -f fichier.csv -o fichier.csv

import argparse
import pandas as pd
import matplotlib.pyplot as plt

# parse_txt_file: str -> DataFrame
def parse_txt_file(file_path):
    freqs = []
    magnitudes = []
    phases = []

    with open(file_path, 'r', encoding='latin-1') as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                freq = float(parts[0])
                magnitude_phase = parts[1].strip('()').split(',')
                magnitude = float(magnitude_phase[0].replace('dB', ''))
                phase = float(magnitude_phase[1].replace('°', ''))

                freqs.append(freq)
                magnitudes.append(magnitude)
                phases.append(phase)

    data = {'Frequency': freqs, 'Magnitude (dB)': magnitudes, 'Phase (°)': phases}
    return pd.DataFrame(data)

# write_csv_file with DataFrame
def write_csv_file(output_path, data):
    data.to_csv(output_path, index=False)

# plot_data with DataFrame
def plot_data(data):
    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('Magnitude (dB)', color=color)
    ax1.plot(data['Frequency'], data['Magnitude (dB)'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Phase (°)', color=color)
    ax2.plot(data['Frequency'], data['Phase (°)'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
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