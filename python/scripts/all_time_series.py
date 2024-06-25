import os
import pandas as pd
import matplotlib.pyplot as plt

def time_series(data_directory, output_directory):
    all_files = [os.path.join(data_directory, f) for f in os.listdir(data_directory) if f.endswith('.csv')]
    
    # Check if there are any files to process
    if not all_files:
        print(f"No CSV files found in the directory: {data_directory}")
        return

    data_frames = []
    for file in all_files:
        try:
            df = pd.read_csv(file)
            df['source'] = os.path.basename(file)  # Track the source file
            data_frames.append(df)
        except pd.errors.ParserError:
            print(f"Error parsing {file}. Skipping.")

    if not data_frames:
        print("No valid data files to process.")
        return

    combined_df = pd.concat(data_frames)
    
    plt.figure(figsize=(12, 10))
    
    plt.subplot(2, 2, 1)
    for name, group in combined_df.groupby('source'):
        plt.plot(group['time'], group['a1'], label=name)
    plt.xlabel('Time (s)')
    plt.ylabel('a1')
    plt.title('a1 over Time')
    plt.grid(True)
    
    plt.subplot(2, 2, 2)
    for name, group in combined_df.groupby('source'):
        plt.plot(group['time'], group['a2'], label=name)
    plt.xlabel('Time (s)')
    plt.ylabel('a2')
    plt.title('a2 over Time')
    plt.grid(True)
    
    plt.subplot(2, 2, 3)
    for name, group in combined_df.groupby('source'):
        plt.plot(group['time'], group['v1'], label=name)
    plt.xlabel('Time (s)')
    plt.ylabel('v1')
    plt.title('v1 over Time')
    plt.grid(True)
    
    plt.subplot(2, 2, 4)
    for name, group in combined_df.groupby('source'):
        plt.plot(group['time'], group['v2'], label=name)
    plt.xlabel('Time (s)')
    plt.ylabel('v2')
    plt.title('v2 over Time')
    plt.grid(True)
    
    plt.tight_layout()
    
    # Save the plot as an image file
    output_file = os.path.join(output_directory, 'combined_time_series.png')
    plt.savefig(output_file)
    print(f"Plot saved to {output_file}")

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
        
        time_series(data_directory, output_directory)
