import os
import pandas as pd

class CSVCombiner:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def combine_csv_files(self, output_file_path):
        dataframes = []

        for filename in os.listdir(self.folder_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(self.folder_path, filename)
                df = pd.read_csv(file_path)
                dataframes.append(df)

        combined_df = pd.concat(dataframes, ignore_index=True)
        combined_df = combined_df.loc[~combined_df.index.duplicated(keep='first')]
        combined_df.to_csv(output_file_path, index=False)
        print(f'Merged CSV file saved to {output_file_path}')