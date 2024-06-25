import os
import pandas as pd
import matplotlib.pyplot as plt

def calculate_mean_and_std(df, column_name):
    grouped = df.groupby('time')[column_name]
    mean = grouped.mean()
    std = grouped.std()
    return mean, std

def plot_with_error_bands(time, mean, std, label):
    plt.plot(time, mean, label=label)
    plt.fill_between(time, mean - std, mean + std, alpha=0.3)

def plot_std_time_series(data_directory, output_directory):
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
    
    mean_a1, std_a1 = calculate_mean_and_std(combined_df, 'a1')
    mean_a2, std_a2 = calculate_mean_and_std(combined_df, 'a2')
    mean_v1, std_v1 = calculate_mean_and_std(combined_df, 'v1')
    mean_v2, std_v2 = calculate_mean_and_std(combined_df, 'v2')
    
    print("Mean a1:", mean_a1.head())
    print("Std a1:", std_a1.head())
    print("Mean a2:", mean_a2.head())
    print("Std a2:", std_a2.head())
    print("Mean v1:", mean_v1.head())
    print("Std v1:", std_v1.head())
    print("Mean v2:", mean_v2.head())
    print("Std v2:", std_v2.head())
    
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plot_with_error_bands(time, mean_a1, std_a1, 'a1')
    plt.xlabel('Time (s)')
    plt.ylabel('a1')
    plt.title('Mean and Std of a1 over Time')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 2, 2)
    plot_with_error_bands(time, mean_a2, std_a2, 'a2')
    plt.xlabel('Time (s)')
    plt.ylabel('a2')
    plt.title('Mean and Std of a2 over Time')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 2, 3)
    plot_with_error_bands(time, mean_v1, std_v1, 'v1')
    plt.xlabel('Time (s)')
    plt.ylabel('v1')
    plt.title('Mean and Std of v1 over Time')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 2, 4)
    plot_with_error_bands(time, mean_v2, std_v2, 'v2')
    plt.xlabel('Time (s)')
    plt.ylabel('v2')
    plt.title('Mean and Std of v2 over Time')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    
    # Save the plot as an image file
    output_file = os.path.join(output_directory, 'mean_std_error_bands.png')
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
