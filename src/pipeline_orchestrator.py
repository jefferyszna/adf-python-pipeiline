"""
Azure Data Factory Pipeline Orchestrator
Main entry point for running the ADF pipeline.
"""

import os
import json
import logging
from datetime import datetime
from src.data_processing import DataProcessor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_pipeline(config_path: str) -> dict:
    """
    Run the data pipeline with configuration from JSON file.
    
    Args:
        config_path: Path to pipeline configuration JSON
        
    Returns:
        Pipeline execution results
    """
    try:
        # Load configuration
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        logger.info(f"Pipeline started with config: {config_path}")
        
        # Initialize processor
        processor = DataProcessor(
            input_path=config['input_path'],
            output_path=config['output_path']
        )
        
        # Execute pipeline
        result = processor.process()
        
        # Log execution
        execution_log = {
            "pipeline_name": config.get('pipeline_name', 'default'),
            "execution_time": datetime.now().isoformat(),
            "result": result
        }
        
        # Write execution log
        log_dir = config.get('log_path', 'logs')
        os.makedirs(log_dir, exist_ok=True)
        
        log_file = os.path.join(
            log_dir,
            f"execution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
        
        with open(log_file, 'w') as f:
            json.dump(execution_log, f, indent=2)
        
        logger.info(f"Execution log saved to {log_file}")
        return result
        
    except FileNotFoundError as e:
        logger.error(f"Configuration file not found: {e}")
        return {"status": "failed", "error": str(e)}
    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
        return {"status": "failed", "error": str(e)}


if __name__ == "__main__":
    # Run with default config
    result = run_pipeline("config/pipeline_config.json")
    print(json.dumps(result, indent=2))
