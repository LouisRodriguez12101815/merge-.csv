import os
import glob
import pandas as pd

# Change this to the path of your CSV files
path = 'path_to_csv_files'
all_files = glob.glob(os.path.join(path, "*.csv"))

all_df = []
for f in all_files:
    df = pd.read_csv(f, index_col=None, header=0)
    all_df.append(df)

merged_df = pd.concat(all_df, axis=0, ignore_index=True)
merged_df.to_csv("merged.csv", index=False)
