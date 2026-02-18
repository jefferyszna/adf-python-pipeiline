# Azure Data Factory Python Pipeline - Deployment Guide

## Overview
This is a complete Azure Data Factory (ADF) Python-based data processing pipeline. It reads CSV data, cleans it, transforms it, validates it, and writes the output.

## Project Structure
```
├── src/
│   ├── data_processing.py      # Core data processing logic
│   └── pipeline_orchestrator.py # Pipeline orchestration
├── config/
│   └── pipeline_config.json    # Pipeline configuration
├── data/
│   ├── input.csv              # Sample input data
│   └── output.csv             # Processed output (generated)
├── tests/
│   └── test_pipeline.py        # Unit tests
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
└── README.md                  # This file
```

## Prerequisites
- Python 3.8 or higher
- Azure Account with active subscription
- Azure CLI installed
- Git installed
- GitHub or Azure DevOps account (for PR)

## Local Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd adf-python-pipeline
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Pipeline Locally
```bash
python src/pipeline_orchestrator.py
```

## Azure Deployment Steps

### Step 1: Create Azure Resources

#### 1.1 Create Resource Group
```bash
az group create \
  --name myResourceGroup \
  --location eastus
```

#### 1.2 Create Storage Account
```bash
az storage account create \
  --name mystorageaccount \
  --resource-group myResourceGroup \
  --location eastus \
  --sku Standard_LRS
```

#### 1.3 Create Data Factory
```bash
az datafactory create \
  --resource-group myResourceGroup \
  --factory-name myADFInstance \
  --location eastus
```

### Step 2: Set Up Authentication

Create an `.env` file with your Azure credentials:
```
AZURE_SUBSCRIPTION_ID=your-subscription-id
AZURE_RESOURCE_GROUP=myResourceGroup
AZURE_DATA_FACTORY_NAME=myADFInstance
AZURE_STORAGE_ACCOUNT_NAME=mystorageaccount
AZURE_STORAGE_ACCOUNT_KEY=your-storage-key
```

### Step 3: Deploy Pipeline to ADF

Use Azure CLI or Python SDK to deploy:

```python
# Example deployment script (deploy_to_azure.py)
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
import json

credential = DefaultAzureCredential()
client = DataFactoryManagementClient(
    credential,
    subscription_id=os.environ['AZURE_SUBSCRIPTION_ID']
)

# Read pipeline definition
with open('config/pipeline_config.json') as f:
    pipeline_def = json.load(f)

# Create/Update pipeline
client.pipelines.create_or_update(
    resource_group_name=os.environ['AZURE_RESOURCE_GROUP'],
    factory_name=os.environ['AZURE_DATA_FACTORY_NAME'],
    pipeline_name=pipeline_def['pipeline_name'],
    pipeline=pipeline_def
)
```

## Running Tests

```bash
python -m pytest tests/ -v
```

## Creating a Pull Request

### For GitHub:

1. **Create a fork** (if not already a collaborator)
   - Go to the repository on GitHub
   - Click "Fork" in the top right

2. **Create a new branch**
   ```bash
   git checkout -b feature/add-python-pipeline
   ```

3. **Make your changes and commit**
   ```bash
   git add .
   git commit -m "feat: add Python-based ADF data pipeline

   - Implement DataProcessor class for CSV processing
   - Add data cleaning, transformation, and validation
   - Create pipeline orchestrator
   - Add sample data and configuration"
   ```

4. **Push to your fork**
   ```bash
   git push origin feature/add-python-pipeline
   ```

5. **Create Pull Request**
   - Go to GitHub
   - Click "Compare & pull request"
   - Add title: "Add Python ADF Data Pipeline"
   - Add description with pipeline details
   - Click "Create pull request"

### For Azure DevOps:

1. **Create a new branch**
   ```bash
   git checkout -b feature/add-python-pipeline
   ```

2. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: add Python-based ADF data pipeline"
   git push origin feature/add-python-pipeline
   ```

3. **Create Pull Request in Azure DevOps**
   - Go to Repos → Pull requests
   - Click "New pull request"
   - Select your branch
   - Add description and reviewers
   - Click "Create"

## Pipeline Features

✅ **Data Reading** - Reads CSV files from configured path
✅ **Data Cleaning** - Removes duplicates and null values
✅ **Data Transformation** - Normalizes and enriches data
✅ **Data Validation** - Ensures data quality
✅ **Error Handling** - Comprehensive logging and error reporting
✅ **Execution Tracking** - Logs all executions with timestamps

## Monitoring & Logs

Execution logs are saved in `logs/` directory with timestamps:
```
logs/
├── execution_20260218_093045.json
└── execution_20260218_120130.json
```

Check recent execution:
```bash
ls -lt logs/ | head -1
cat logs/<latest-execution>.json
```

## Troubleshooting

### Issue: ModuleNotFoundError
**Solution**: Ensure virtual environment is activated and dependencies installed
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: Azure Authentication Failed
**Solution**: Check `.env` file and ensure credentials are correct
```bash
az login
az account show
```

### Issue: Input file not found
**Solution**: Ensure input CSV exists at the configured path
```bash
ls data/input.csv
```

## Next Steps

1. ✅ Set up local development environment
2. ✅ Test pipeline with sample data
3. ✅ Deploy to Azure
4. ✅ Create and merge pull request
5. ⏳ Set up CI/CD pipeline with GitHub Actions or Azure Pipelines
6. ⏳ Add more complex transformations as needed

## Additional Resources

- [Azure Data Factory Documentation](https://docs.microsoft.com/azure/data-factory/)
- [Python Pandas Documentation](https://pandas.pydata.org/docs/)
- [Azure Storage Documentation](https://docs.microsoft.com/azure/storage/)
- [Git & GitHub Guide](https://guides.github.com/)

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review Azure Data Factory documentation
3. Check GitHub Issues
4. Contact the team

---
**Last Updated**: February 18, 2026
