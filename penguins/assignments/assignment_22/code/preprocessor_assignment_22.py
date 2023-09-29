
import pandas as pd
from pathlib import Path


def capitalize_island(dataframe):
    """Island column values to uppercase"""
    dataframe["island"] = dataframe["island"].str.upper()  # so it's different from default
    return dataframe


def preprocess(input_filepath, output_filepath):
    """Process a single CSV file and save to the specified output filepath"""
    data = pd.read_csv(input_filepath)
    processed_data = capitalize_island(data)
    processed_data.to_csv(output_filepath, index=False)
    print(f"Processed {input_filepath} and saved to {output_filepath}")


def process_all_files(input_dir, output_dir):
    """Process all CSV files in the input directory and save to the output directory"""
    input_dir_path = Path(input_dir)
    for filename in input_dir_path.iterdir():
        if filename.suffix == '.csv':  # only process .csv files
            input_filepath = input_dir_path / filename.name
            output_filepath = Path(output_dir) / filename.name
            preprocess(input_filepath, output_filepath)


if __name__ == "__main__":

    # default paths for SageMaker Processing
    BASE_DIRECTORY = Path("/opt/ml/processing")
    DATA_DIRECTORY = BASE_DIRECTORY / "input"
    OUTPUT_DIRECTORY = BASE_DIRECTORY / "output"
    
    process_all_files(DATA_DIRECTORY, OUTPUT_DIRECTORY)
