"""
Azure Data Factory Python Data Processing Module
This module handles data transformation and processing for the ADF pipeline.
"""

import pandas as pd
import logging
from datetime import datetime
import os
import json
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DataProcessor:
    """Process and transform CSV data."""
    
    def __init__(self, input_path: str, output_path: str):
        """
        Initialize the data processor.
        
        Args:
            input_path: Path to input CSV file
            output_path: Path to output CSV file
        """
        self.input_path = input_path
        self.output_path = output_path
        self.df = None
        
    def read_csv(self) -> pd.DataFrame:
        """Read CSV file from input path."""
        try:
            logger.info(f"Reading CSV from {self.input_path}")
            self.df = pd.read_csv(self.input_path)
            logger.info(f"Successfully read {len(self.df)} rows")
            return self.df
        except FileNotFoundError:
            logger.error(f"Input file not found: {self.input_path}")
            raise
        except Exception as e:
            logger.error(f"Error reading CSV: {str(e)}")
            raise
    
    def clean_data(self) -> pd.DataFrame:
        """Clean and validate data."""
        if self.df is None:
            raise ValueError("No data loaded. Call read_csv() first.")
        
        logger.info("Cleaning data...")
        
        # Remove duplicates
        self.df = self.df.drop_duplicates()
        logger.info(f"Removed duplicates. Rows: {len(self.df)}")
        
        # Handle missing values
        self.df = self.df.dropna()
        logger.info(f"Removed rows with missing values. Rows: {len(self.df)}")
        
        return self.df
    
    def transform_data(self) -> pd.DataFrame:
        """Apply transformations to the data."""
        if self.df is None:
            raise ValueError("No data loaded. Call read_csv() first.")
        
        logger.info("Transforming data...")
        
        # Add processing timestamp
        self.df['processed_timestamp'] = datetime.now().isoformat()
        
        # Convert column names to lowercase
        self.df.columns = self.df.columns.str.lower()
        
        # Trim whitespace from string columns
        for col in self.df.select_dtypes(include=['object']).columns:
            self.df[col] = self.df[col].str.strip()
        
        logger.info("Data transformation complete")
        return self.df
    
    def validate_data(self) -> bool:
        """Validate the processed data."""
        if self.df is None:
            raise ValueError("No data loaded.")
        
        logger.info("Validating data...")
        
        # Check for empty dataframe
        if len(self.df) == 0:
            logger.warning("Dataframe is empty after processing")
            return False
        
        # Check for null values
        if self.df.isnull().any().any():
            logger.warning("NULL values found in dataframe")
            return False
        
        logger.info("Data validation passed")
        return True
    
    def write_csv(self) -> None:
        """Write processed data to output CSV."""
        if self.df is None:
            raise ValueError("No data to write.")
        
        try:
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
            
            logger.info(f"Writing CSV to {self.output_path}")
            self.df.to_csv(self.output_path, index=False)
            logger.info("CSV write successful")
        except Exception as e:
            logger.error(f"Error writing CSV: {str(e)}")
            raise
    
    def process(self) -> dict:
        """
        Execute the complete data pipeline.
        
        Returns:
            Dictionary with processing results
        """
        try:
            logger.info("Starting data pipeline...")
            start_time = datetime.now()
            
            # Execute pipeline steps
            self.read_csv()
            self.clean_data()
            self.transform_data()
            
            if not self.validate_data():
                raise ValueError("Data validation failed")
            
            self.write_csv()
            
            end_time = datetime.now()
            duration = (end_time - start_time).total_seconds()
            
            result = {
                "status": "success",
                "rows_processed": len(self.df),
                "duration_seconds": duration,
                "output_path": self.output_path,
                "timestamp": datetime.now().isoformat()
            }
            
            logger.info(f"Pipeline completed successfully. Duration: {duration}s")
            return result
            
        except Exception as e:
            logger.error(f"Pipeline failed: {str(e)}")
            return {
                "status": "failed",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }


if __name__ == "__main__":
    # Example usage
    input_file = "data/input.csv"
    output_file = "data/output.csv"
    
    processor = DataProcessor(input_file, output_file)
    result = processor.process()
    
    print(json.dumps(result, indent=2))
