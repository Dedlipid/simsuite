import os
import pandas as pd
import matplotlib.pyplot as plt

def time_series(data_directory, output_directory):
    for f in os.listdir(data_directory) :
        if f.endswith('.csv'):
            print(f)
    all_files = [os.path.join(data_directory, f) for f in os.listdir(data_directory) if f.endswith('.csv')]
    
    # Check if there are any files to process
    if not all_files:
        print(f"No CSV files found in the directory: {data_directory}")
        return
    
    images_saved = False
    
    for file in all_files:
        try:
            df = pd.read_csv(file)
        except pd.errors.ParserError:
            print(f"Error parsing {file}. Skipping.")
            continue
        
        if not os.path.exists(file):
            print(f"File {file} does not exist. Skipping.")
            continue
        
        base_filename = os.path.basename(file).replace('.csv', '')

        plt.figure(figsize=(10, 6))
        
        plt.subplot(2, 2, 1)
        plt.plot(df['time'], df['a1'], label='a1')
        plt.xlabel('Time (s)')
        plt.ylabel('a1')
        plt.title('a1 over Time')
        plt.legend()
        plt.grid(True)
        
        plt.subplot(2, 2, 2)
        plt.plot(df['time'], df['a2'], label='a2')
        plt.xlabel('Time (s)')
        plt.ylabel('a2')
        plt.title('a2 over Time')
        plt.legend()
        plt.grid(True)
        
        plt.subplot(2, 2, 3)
        plt.plot(df['time'], df['v1'], label='v1')
        plt.xlabel('Time (s)')
        plt.ylabel('v1')
        plt.title('v1 over Time')
        plt.legend()
        plt.grid(True)
        
        plt.subplot(2, 2, 4)
        plt.plot(df['time'], df['v2'], label='v2')
        plt.xlabel('Time (s)')
        plt.ylabel('v2')
        plt.title('v2 over Time')
        plt.legend()
        plt.grid(True)
        
        plt.tight_layout()
        
        # Save the plot as an image file
        output_file = os.path.join(output_directory, f'{base_filename}_time_series.png')
        plt.savefig(output_file)
        print(f"Plot saved to {output_file}")
        images_saved = True
        
        plt.close()
    
    if not images_saved:
        print("No images were saved.")

if __name__ == "__main__":
    data_directory = 'data'
    output_directory = 'python/output/time_series'
    
    # Check if the data directory exists
    if not os.path.exists(data_directory):
        print(f"Data directory does not exist: {data_directory}")
    else:
        # Ensure the output directory exists
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        time_series(data_directory, output_directory)
