import os
from pathlib import Path
import pandas as pd
from dataclasses import dataclass,field
from movieRecommender.logging import logger
from typing import List, Dict

@dataclass
class ValidationConfig:
    root_dir: Path
    dataset_name: str
    required_columns: List[str]
    data_types: Dict[str, type]
    report_file: str = field(init=False)

    def __post_init__(self):
        self.report_file = os.path.join(self.root_dir, f"{self.dataset_name}_validation_report.txt")

    def validate_dataset(self) -> bool:
        """Validate the dataset based on the configuration."""
        dataset_path = os.path.join(self.root_dir, self.dataset_name)
        if not os.path.exists(dataset_path):
            logger.error(f"Dataset not found at {dataset_path}")
            self.write_report(f"Dataset not found at {dataset_path}")
            return False

        # Get a list of all CSV files in the dataset directory
        csv_files = [f for f in os.listdir(dataset_path) if f.endswith('.csv')]

        if not csv_files:
            logger.error(f"No CSV files found in {dataset_path}")
            self.write_report(f"No CSV files found in {dataset_path}")
            return False

        # Validate each CSV file
        for csv_file in csv_files:
            file_path = os.path.join(dataset_path, csv_file)
            logger.info(f"Validating {csv_file}")
            data = pd.read_csv(file_path)

            if not self.validate_columns(data):
                return False
            if not self.validate_data_types(data):
                return False

        logger.info("Dataset validation successful!")
        self.write_report("Dataset validation successful!")
        return True

    def validate_columns(self, data: pd.DataFrame) -> bool:
        """Validate the required columns in the dataset."""
        missing_columns = [col for col in self.required_columns if col not in data.columns]
        if missing_columns:
            logger.error(f"Missing required columns in {data.shape[0]} rows: {', '.join(missing_columns)}")
            self.write_report(f"Missing required columns in {data.shape[0]} rows: {', '.join(missing_columns)}")
            return False
        return True

    def validate_data_types(self, data: pd.DataFrame) -> bool:
        """Validate the data types of the columns in the dataset."""
        for column, data_type in self.data_types.items():
            if column not in data.columns:
                continue
            if data[column].dtype != data_type:
                logger.error(f"Invalid data type for column '{column}' in {data.shape[0]} rows. Expected: {data_type}, Actual: {data[column].dtype}")
                self.write_report(f"Invalid data type for column '{column}' in {data.shape[0]} rows. Expected: {data_type}, Actual: {data[column].dtype}")
                return False
        return True
    
    def write_report(self, message: str):
        """Write the validation report to a file."""
        with open(self.report_file, "a") as f:
            f.write(message + "\n")
