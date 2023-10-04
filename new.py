import tarfile
import pandas as pd

# Full path to your .tar.gz file
tar_gz_file_path = "C:/Users/Administrator/cat/amazon-massive-dataset-1.1_CAT1.tar.gz"

# Destination folder for extraction
destination_folder = "data_folder"

# Open the .tar.gz file and extract its contents
with tarfile.open(tar_gz_file_path, "r:gz") as tar:
    tar.extractall(path=destination_folder)

# Verify the contents of the destination folder

# Now, you can work with the extracted Excel file(s)
# Assuming the extracted file is in the "data_folder" and has a specific name, e.g., "data.xlsx"

# Load the dataset from the extracted Excel file
dataset = pd.read_excel(f"{destination_folder}/data.xlsx")

# Iterate through unique language ids
unique_languages = dataset['id'].unique()

for lang_id in unique_languages:
    lang_data = dataset[dataset['id'] == lang_id][['id', 'utt', 'annot_utt']]
    lang_data.to_excel(f"{destination_folder}/en-{lang_id}.xlsx", index=False)
