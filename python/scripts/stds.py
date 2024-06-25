import os
import pandas as pd
import matplotlib.pyplot as plt

def calculate_std(df, column_name):
    return df.groupby('time')[column_name].std()

def calculate_mean(df, column_name):
    return df.groupby('time')[column_name].mean()

def calculate_normalized_std(df, column_name):
    std = calculate_std(df, column_name)
    mean = calculate_mean(df, column_name)
    return std / mean

def calculate_rolling_normalized_std(df, column_name, window_size):
    std = calculate_std(df, column_name)
    mean = calculate_mean(df, column_name)
    rolling_std = std.rolling(window=window_size).std()
    rolling_mean = mean.rolling(window=window_size).mean()
    return rolling_std / rolling_mean

def plot_std_time_series(data_directory, output_directory, window_size=10):
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
    
    time = combined_df['time'].unique()
    normalized_std_a1 = calculate_normalized_std(combined_df, 'a1')
    normalized_std_a2 = calculate_normalized_std(combined_df, 'a2')
    normalized_std_v1 = calculate_normalized_std(combined_df, 'v1')
    normalized_std_v2 = calculate_normalized_std(combined_df, 'v2')
    
    rolling_normalized_std_a1 = calculate_rolling_normalized_std(combined_df, 'a1', window_size)
    rolling_normalized_std_a2 = calculate_rolling_normalized_std(combined_df, 'a2', window_size)
    rolling_normalized_std_v1 = calculate_rolling_normalized_std(combined_df, 'v1', window_size)
    rolling_normalized_std_v2 = calculate_rolling_normalized_std(combined_df, 'v2', window_size)
    
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.plot(time, normalized_std_a1, label='avg std/mean(a1)')
    plt.plot(time, rolling_normalized_std_a1, label='rolling std/mean(a1)', linestyle='--')
    plt.xlabel('Time (s)')
    plt.ylabel('Normalized Standard Deviation')
    plt.title('Normalized Standard Deviation of a1 over Time')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 2, 2)
    plt.plot(time, normalized_std_a2, label='avg std/mean(a2)')
    plt.plot(time, rolling_normalized_std_a2, label='rolling std/mean(a2)', linestyle='--')
    plt.xlabel('Time (s)')
    plt.ylabel('Normalized Standard Deviation')
    plt.title('Normalized Standard Deviation of a2 over Time')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 2, 3)
    plt.plot(time, normalized_std_v1, label='avg std/mean(v1)')
    plt.plot(time, rolling_normalized_std_v1, label='rolling std/mean(v1)', linestyle='--')
    plt.xlabel('Time (s)')
    plt.ylabel('Normalized Standard Deviation')
    plt.title('Normalized Standard Deviation of v1 over Time')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 2, 4)
    plt.plot(time, normalized_std_v2, label='avg std/mean(v2)')
    plt.plot(time, rolling_normalized_std_v2, label='rolling std/mean(v2)', linestyle='--')
    plt.xlabel('Time (s)')
    plt.ylabel('Normalized Standard Deviation')
    plt.title('Normalized Standard Deviation of v2 over Time')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    
    # Save the plot as an image file
    output_file = os.path.join(output_directory, 'normalized_std_time_series.png')
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
        
        plot_std_time_series(data_directory, output_directory)
