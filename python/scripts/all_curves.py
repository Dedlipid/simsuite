import os
import pandas as pd
import matplotlib.pyplot as plt

def load_and_plot_time_series(data_directory, output_directory):
    all_files = [os.path.join(data_directory, f) for f in os.listdir(data_directory) if f.endswith('.csv')]
    
    # Check if there are any files to process
    if not all_files:
        print(f"No CSV files found in the directory: {data_directory}")
        return
    
    data_frames = []
    for file in all_files:
        try:
            df = pd.read_csv(file)
            data_frames.append(df)
        except pd.errors.ParserError:
            print(f"Error parsing {file}. Skipping.")
    
    if not data_frames:
        print("No valid data files to process.")
        return
    
    combined_df = pd.concat(data_frames)
    
    time = combined_df['time']
    
    plt.figure(figsize=(12, 10))
    
    plt.subplot(3, 1, 1)
    for file in all_files:
        df = pd.read_csv(file)
        plt.plot(df['time'], df['a1'], label=f'a1 from {os.path.basename(file)}')
    plt.xlabel('Time (s)')
    plt.ylabel('a1')
    plt.title('a1 over Time')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(3, 1, 2)
    for file in all_files:
        df = pd.read_csv(file)
        plt.plot(df['time'], df['a2'], label=f'a2 from {os.path.basename(file)}')
    plt.xlabel('Time (s)')
    plt.ylabel('a2')
    plt.title('a2 over Time')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(3, 1, 3)
    for file in all_files:
        df = pd.read_csv(file)
        plt.plot(df['time'], df['v1'], label=f'v1 from {os.path.basename(file)}')
    plt.xlabel('Time (s)')
    plt.ylabel('v1')
    plt.title('v1 over Time')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    
    # Save the plot as an image file
    output_file = os.path.join(output_directory, 'time_series.png')
    plt.savefig(output_file)
    print(f"Plot saved to {output_file}")
    plt.show()

if __name__ == "__main__":
    data_directory = 'data'
    output_directory = 'python/output'
    
    # Check if the data directory exists
    if not os.path.exists(data_directory):
        print(f"Data directory does not exist: {data_directory}")
    else:
        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        load_and_plot_time_series(data_directory, output_directory)
