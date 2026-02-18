"""
Unit tests for the ADF data pipeline.
"""

import pytest
import pandas as pd
import os
import tempfile
import json
from src.data_processing import DataProcessor


@pytest.fixture
def temp_dir():
    """Create temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def sample_csv(temp_dir):
    """Create sample CSV for testing."""
    csv_path = os.path.join(temp_dir, 'input.csv')
    data = {
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'email': ['alice@test.com', 'bob@test.com', 'charlie@test.com']
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)
    return csv_path


class TestDataProcessor:
    """Test suite for DataProcessor class."""
    
    def test_initialization(self, temp_dir):
        """Test DataProcessor initialization."""
        input_path = os.path.join(temp_dir, 'input.csv')
        output_path = os.path.join(temp_dir, 'output.csv')
        processor = DataProcessor(input_path, output_path)
        
        assert processor.input_path == input_path
        assert processor.output_path == output_path
        assert processor.df is None
    
    def test_read_csv(self, sample_csv, temp_dir):
        """Test CSV reading functionality."""
        output_path = os.path.join(temp_dir, 'output.csv')
        processor = DataProcessor(sample_csv, output_path)
        df = processor.read_csv()
        
        assert len(df) == 3
        assert list(df.columns) == ['id', 'name', 'email']
        assert processor.df is not None
    
    def test_read_csv_not_found(self, temp_dir):
        """Test error handling for missing file."""
        input_path = os.path.join(temp_dir, 'nonexistent.csv')
        output_path = os.path.join(temp_dir, 'output.csv')
        processor = DataProcessor(input_path, output_path)
        
        with pytest.raises(FileNotFoundError):
            processor.read_csv()
    
    def test_clean_data(self, sample_csv, temp_dir):
        """Test data cleaning functionality."""
        output_path = os.path.join(temp_dir, 'output.csv')
        processor = DataProcessor(sample_csv, output_path)
        processor.read_csv()
        
        df_cleaned = processor.clean_data()
        
        assert len(df_cleaned) > 0
        assert df_cleaned.isnull().sum().sum() == 0
    
    def test_transform_data(self, sample_csv, temp_dir):
        """Test data transformation."""
        output_path = os.path.join(temp_dir, 'output.csv')
        processor = DataProcessor(sample_csv, output_path)
        processor.read_csv()
        
        df_transformed = processor.transform_data()
        
        # Check if timestamp column was added
        assert 'processed_timestamp' in df_transformed.columns
        # Check if column names are lowercase
        assert all(col.islower() for col in df_transformed.columns)
    
    def test_validate_data(self, sample_csv, temp_dir):
        """Test data validation."""
        output_path = os.path.join(temp_dir, 'output.csv')
        processor = DataProcessor(sample_csv, output_path)
        processor.read_csv()
        processor.clean_data()
        
        is_valid = processor.validate_data()
        
        assert is_valid is True
    
    def test_write_csv(self, sample_csv, temp_dir):
        """Test CSV writing functionality."""
        output_path = os.path.join(temp_dir, 'output.csv')
        processor = DataProcessor(sample_csv, output_path)
        processor.read_csv()
        processor.clean_data()
        processor.transform_data()
        
        processor.write_csv()
        
        assert os.path.exists(output_path)
        df_written = pd.read_csv(output_path)
        assert len(df_written) > 0
    
    def test_full_pipeline(self, sample_csv, temp_dir):
        """Test complete pipeline execution."""
        output_path = os.path.join(temp_dir, 'output.csv')
        processor = DataProcessor(sample_csv, output_path)
        
        result = processor.process()
        
        assert result['status'] == 'success'
        assert result['rows_processed'] > 0
        assert result['duration_seconds'] >= 0
        assert os.path.exists(output_path)


class TestPipelineOrchestration:
    """Test suite for pipeline orchestration."""
    
    def test_pipeline_config_format(self):
        """Test pipeline configuration is valid JSON."""
        config_path = 'config/pipeline_config.json'
        
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        assert 'pipeline_name' in config
        assert 'activities' in config
        assert len(config['activities']) > 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
