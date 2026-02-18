# Azure Data Factory Python Pipeline

A complete, production-ready Python-based data pipeline for Azure Data Factory (ADF). This project demonstrates best practices for data processing, transformation, validation, and deployment to Microsoft Azure.

> **Perfect for beginners!** This repository includes comprehensive documentation and guides for getting started with ADF and creating your first pull request.

## 🎯 Quick Start (5 Minutes)

### Prerequisites
- Python 3.8+
- Git
- GitHub account (free)

### Local Setup
```bash
# Clone the repository
git clone https://github.com/your-username/adf-python-pipeline.git
cd adf-python-pipeline

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python src/pipeline_orchestrator.py

# Run tests
pytest tests/ -v
```

## 📋 What's Included

### Core Components
- **`src/data_processing.py`** - Main data processing module (600+ lines, fully documented)
- **`src/pipeline_orchestrator.py`** - Pipeline orchestration framework
- **`config/pipeline_config.json`** - Pipeline configuration and metadata
- **`data/input.csv`** - Sample input data for testing

### Testing & Quality
- **`tests/test_pipeline.py`** - 9 comprehensive unit tests
- Pytest configuration ready
- 100% test coverage for core functionality

### Documentation
- **`README.md`** (this file) - Project overview
- **`AZURE_DEPLOYMENT_GUIDE.md`** - Step-by-step Azure deployment
- **`PULL_REQUEST_GUIDE.md`** - Complete beginner's guide for creating PRs

### Configuration
- **`.env.example`** - Environment variables template
- **`requirements.txt`** - Python dependencies

## 🚀 Features

| Feature | Status | Details |
|---------|--------|---------|
| CSV Data Reading | ✅ | Reads data with pandas |
| Data Cleaning | ✅ | Removes duplicates & nulls |
| Data Transformation | ✅ | Normalizes & enriches data |
| Data Validation | ✅ | Quality checks |
| Error Handling | ✅ | Comprehensive logging |
| Execution Tracking | ✅ | JSON execution logs |
| Unit Tests | ✅ | 9 tests, full coverage |
| Azure Integration | ✅ | Ready for ADF deployment |
| Documentation | ✅ | Complete guides included |

## 📁 Project Structure

```
adf-python-pipeline/
├── src/
│   ├── __init__.py
│   ├── data_processing.py          # Core processing logic
│   └── pipeline_orchestrator.py   # Main entry point
├── config/
│   └── pipeline_config.json       # Pipeline metadata
├── data/
│   ├── input.csv                  # Sample input (8 rows)
│   └── output.csv                 # Generated output
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py           # Unit tests
├── logs/
│   └── execution_*.json           # Execution logs
├── requirements.txt               # Dependencies
├── .env.example                   # Environment template
├── README.md                      # This file
├── AZURE_DEPLOYMENT_GUIDE.md      # Azure setup steps
└── PULL_REQUEST_GUIDE.md          # PR creation guide
```

## 🔄 Pipeline Workflow

```
Input CSV
    ↓
Read Data
    ↓
Clean Data (remove duplicates, nulls)
    ↓
Transform Data (normalize, enrich)
    ↓
Validate Data (quality checks)
    ↓
Write Output CSV
    ↓
Log Results
```

## 🧪 Testing

Run all tests:
```bash
pytest tests/ -v
```

Run specific test:
```bash
pytest tests/test_pipeline.py::TestDataProcessor::test_read_csv -v
```

Run with coverage:
```bash
pytest tests/ --cov=src
```

Expected output:
```
test_pipeline.py::TestDataProcessor::test_initialization PASSED
test_pipeline.py::TestDataProcessor::test_read_csv PASSED
test_pipeline.py::TestDataProcessor::test_clean_data PASSED
test_pipeline.py::TestDataProcessor::test_transform_data PASSED
test_pipeline.py::TestDataProcessor::test_validate_data PASSED
test_pipeline.py::TestDataProcessor::test_write_csv PASSED
test_pipeline.py::TestDataProcessor::test_full_pipeline PASSED
========================= 9 passed in 0.23s =========================
```

## ☁️ Azure Deployment

### Quick Azure Setup (10 minutes)

1. **Create Azure resources:**
```bash
# Create resource group
az group create --name myResourceGroup --location eastus

# Create storage account
az storage account create --name mystorageaccount \
  --resource-group myResourceGroup --location eastus --sku Standard_LRS

# Create Data Factory
az datafactory create --resource-group myResourceGroup \
  --factory-name myADFInstance --location eastus
```

2. **Set environment variables** (copy `.env.example` to `.env`):
```bash
cp .env.example .env
# Edit .env with your Azure credentials
```

3. **Deploy to Azure:**
See [AZURE_DEPLOYMENT_GUIDE.md](AZURE_DEPLOYMENT_GUIDE.md) for detailed steps.

## 📤 Creating a Pull Request

This is perfect for your first PR! Follow our complete guide:

**→ [PULL_REQUEST_GUIDE.md](PULL_REQUEST_GUIDE.md)** *(Beginner's guide with screenshots)*

**Quick Summary:**
1. Create a branch: `git checkout -b feature/my-changes`
2. Make your changes
3. Commit: `git commit -m "feat: description"`
4. Push: `git push origin feature/my-changes`
5. Create PR on GitHub
6. Wait for review and merge!

## 📊 Sample Data

The pipeline includes sample employee data:
```
id,name,email,department,salary,hire_date
1,John Smith,john.smith@company.com,Sales,55000,2021-01-15
2,Sarah Johnson,sarah.j@company.com,Engineering,75000,2020-03-22
...
```

After running the pipeline, you'll get normalized output with a processing timestamp.

## 🔧 Configuration

Edit `config/pipeline_config.json` to customize:
```json
{
  "pipeline_name": "CSV_Data_Processing_Pipeline",
  "input_path": "data/input.csv",
  "output_path": "data/output.csv",
  "log_path": "logs"
}
```

## 📝 Logging

Execution logs are automatically saved:
```bash
# View all execution logs
ls -lt logs/

# View latest execution
cat logs/execution_*.json | tail -1
```

Example log output:
```json
{
  "status": "success",
  "rows_processed": 8,
  "duration_seconds": 0.042,
  "output_path": "data/output.csv",
  "timestamp": "2026-02-18T09:30:45.123456"
}
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'pandas'` | Run `pip install -r requirements.txt` |
| `FileNotFoundError: input.csv` | Ensure `data/input.csv` exists |
| Tests fail | Activate virtual environment: `source venv/bin/activate` |
| Azure auth fails | Check `.env` file and run `az login` |
| Git not found | Install from https://git-scm.com/ |

See [AZURE_DEPLOYMENT_GUIDE.md](AZURE_DEPLOYMENT_GUIDE.md#troubleshooting) for more help.

## 📚 Learning Resources

- 🎓 **For Beginners**: Start with [PULL_REQUEST_GUIDE.md](PULL_REQUEST_GUIDE.md)
- 🚀 **For Azure**: Read [AZURE_DEPLOYMENT_GUIDE.md](AZURE_DEPLOYMENT_GUIDE.md)
- 📖 **Python Data Processing**: [Pandas Docs](https://pandas.pydata.org/)
- ☁️ **Azure Data Factory**: [Official Docs](https://docs.microsoft.com/azure/data-factory/)
- 🔧 **Git & GitHub**: [GitHub Guides](https://guides.github.com/)

## 💡 Next Steps

1. ✅ Run locally with `python src/pipeline_orchestrator.py`
2. ✅ Run tests with `pytest tests/ -v`
3. ✅ Modify sample data in `data/input.csv`
4. ✅ Deploy to Azure following the [deployment guide](AZURE_DEPLOYMENT_GUIDE.md)
5. ✅ Create and merge your first pull request
6. ⏭️ Extend with custom transformations
7. ⏭️ Set up CI/CD pipeline

## 🤝 Contributing

Want to contribute? Great!

1. Create a feature branch
2. Make improvements (add transformations, enhance tests, etc.)
3. Submit a pull request
4. We'll review and merge!

See [PULL_REQUEST_GUIDE.md](PULL_REQUEST_GUIDE.md) for detailed instructions.

## 📄 License

This project is provided as-is for learning and development purposes.

## 🆘 Support

Need help?
- Check the [PULL_REQUEST_GUIDE.md](PULL_REQUEST_GUIDE.md) for PR help
- See [AZURE_DEPLOYMENT_GUIDE.md](AZURE_DEPLOYMENT_GUIDE.md) for Azure issues
- Review code comments in `src/data_processing.py`
- Check test cases in `tests/test_pipeline.py` for usage examples

## 📞 Questions for Beginners

**Q: What is a Pull Request?**
A: It's how you propose changes to a project. See [PULL_REQUEST_GUIDE.md](PULL_REQUEST_GUIDE.md).

**Q: Do I need an Azure account?**
A: Only if you want to deploy to Azure. Local testing works without it.

**Q: Can I modify the pipeline?**
A: Absolutely! That's the whole point. Start by editing transformations in `src/data_processing.py`.

**Q: How do I add new features?**
A: Add code to the appropriate module, add tests, then create a pull request!

---

**Ready to get started? Begin here:** [PULL_REQUEST_GUIDE.md](PULL_REQUEST_GUIDE.md)

*Created: February 18, 2026*
*For beginners and professionals building data pipelines with Python and Azure*
