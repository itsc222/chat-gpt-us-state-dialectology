import os
import glob
import polars as pl

def combine_csv_files(folder_path, output_filename):
    # Get a list of all CSV files in the specified folder
    csv_files = glob.glob(f"{folder_path}/*.csv")

    if not csv_files:
        print("No CSV files found in the specified folder.")
        return

    # Create an empty DataFrame to store the combined data
    combined_df = pl.DataFrame()

    # Loop through each CSV file and concatenate its data to the combined DataFrame
    for file in csv_files:
        df = pl.read_csv(file)
        combined_df = combined_df.vstack(df)

    # Save the combined DataFrame to a new CSV file
    combined_df.write_csv(output_filename)
    print(f"Combined CSV file saved as {output_filename}")

# Example usage:
combine_csv_files("/Users/ischneid/chat-gpt-us-state-dialectology/state-dialect-dfs", "/Users/ischneid/chat-gpt-us-state-dialectology/full_table.csv")
