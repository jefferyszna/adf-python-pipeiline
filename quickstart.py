#!/usr/bin/env python
"""
Quick start script for the ADF Python pipeline.
Run this script to test the pipeline with sample data.
"""

import os
import sys
import json
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.data_processing import DataProcessor


def main():
    """Run the pipeline with sample data."""
    
    print("\n" + "="*60)
    print("Azure Data Factory Python Pipeline - Quick Start")
    print("="*60 + "\n")
    
    # Paths
    input_path = "data/input.csv"
    output_path = "data/output.csv"
    
    print(f"📦 Input file: {input_path}")
    print(f"📄 Output file: {output_path}\n")
    
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"❌ Error: Input file not found: {input_path}")
        print("\nMake sure you have the sample data file or create one.")
        return False
    
    print("🚀 Starting pipeline...\n")
    print("-" * 60)
    
    try:
        # Create processor
        processor = DataProcessor(input_path, output_path)
        
        # Run the full pipeline
        result = processor.process()
        
        print("-" * 60 + "\n")
        
        # Display results
        if result['status'] == 'success':
            print("✅ Pipeline executed successfully!\n")
            print(f"📊 Statistics:")
            print(f"   - Rows processed: {result['rows_processed']}")
            print(f"   - Duration: {result['duration_seconds']:.3f} seconds")
            print(f"   - Output saved to: {result['output_path']}\n")
            
            # Show preview of output
            if os.path.exists(output_path):
                print("📋 Output preview (first 3 rows):")
                print("-" * 60)
                try:
                    import pandas as pd
                    df = pd.read_csv(output_path)
                    print(df.head(3).to_string())
                    print("-" * 60 + "\n")
                except Exception as e:
                    print(f"Could not read output: {e}\n")
            
            return True
        else:
            print(f"❌ Pipeline failed: {result['error']}\n")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}\n")
        import traceback
        traceback.print_exc()
        return False


def print_help():
    """Print help information."""
    print("\n📖 Quick Start Guide:")
    print("-" * 60)
    print("1. Run this script to test the pipeline:")
    print("   python quickstart.py\n")
    
    print("2. Check the output:")
    print("   - Output file: data/output.csv")
    print("   - Execution log: logs/execution_*.json\n")
    
    print("3. Run tests:")
    print("   pytest tests/ -v\n")
    
    print("4. Deploy to Azure:")
    print("   See AZURE_DEPLOYMENT_GUIDE.md\n")
    
    print("5. Create a Pull Request:")
    print("   See PULL_REQUEST_GUIDE.md\n")
    print("-" * 60 + "\n")


if __name__ == "__main__":
    
    # Show help message
    print_help()
    
    # Run the pipeline
    success = main()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)
