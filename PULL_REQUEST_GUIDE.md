# PULL REQUEST GUIDE - Complete Beginner's Guide

## What is a Pull Request (PR)?

A Pull Request is a way to propose changes to a project. Think of it as:
- **Your Changes**: Code you've written locally
- **Review**: Other developers review and approve your changes
- **Merge**: If approved, your changes are added to the main project

## Step-by-Step: Creating Your First Pull Request

### ✅ STEP 1: Prepare Locally

1. **Navigate to your project**
```bash
cd adf-python-pipeline
```

2. **Activate virtual environment**
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Verify everything works**
```bash
python src/pipeline_orchestrator.py
python -m pytest tests/ -v
```

### ✅ STEP 2: Set Up Git and GitHub

1. **Install Git** (if not already installed)
   - Download from https://git-scm.com/

2. **Configure Git** (one-time setup)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

3. **Create GitHub Account** (if you don't have one)
   - Go to https://github.com/
   - Sign up for free

### ✅ STEP 3: Get the Repository Ready

**Option A: If you're a collaborator on an existing repo**
```bash
git clone https://github.com/your-username/adf-python-pipeline.git
cd adf-python-pipeline
```

**Option B: If starting fresh (create new repo on GitHub)**
1. Go to https://github.com/new
2. Create repository named "adf-python-pipeline"
3. Clone it:
```bash
git clone https://github.com/your-username/adf-python-pipeline.git
cd adf-python-pipeline
```

### ✅ STEP 4: Create a Feature Branch

Always create a new branch for your changes (never commit directly to `main`):

```bash
git checkout -b feature/add-python-adf-pipeline
```

**Branch naming convention:**
- `feature/` - for new features
- `fix/` - for bug fixes
- `docs/` - for documentation
- `refactor/` - for code improvements

### ✅ STEP 5: Add Your Changes

Copy all the files we created into your local repository:

```bash
# After running our setup, your directory should have:
# src/
# config/
# data/
# tests/
# requirements.txt
# AZURE_DEPLOYMENT_GUIDE.md
# .env.example
```

Check what files changed:
```bash
git status
```

### ✅ STEP 6: Stage Your Changes

Add all files to Git:
```bash
git add .
```

Or add specific files:
```bash
git add src/data_processing.py
git add config/pipeline_config.json
```

### ✅ STEP 7: Commit Your Changes

Write a clear commit message describing what you did:

```bash
git commit -m "feat: add Python-based ADF data pipeline

- Implement DataProcessor class for CSV processing
- Add data cleaning, transformation, and validation steps
- Create pipeline orchestrator for coordinating activities
- Add comprehensive unit tests with pytest
- Include deployment guide for Azure integration
- Add sample data and pipeline configuration"
```

**Good commit messages:**
- First line: One-liner summary (50 chars max)
- Blank line
- Details explaining why, not what (3-5 bullets)

### ✅ STEP 8: Push to GitHub

Upload your changes to GitHub:
```bash
git push origin feature/add-python-adf-pipeline
```

You'll see output like:
```
Counting objects: 10, done.
...
To https://github.com/your-username/adf-python-pipeline.git
 * [new branch]      feature/add-python-adf-pipeline -> feature/add-python-adf-pipeline
```

### ✅ STEP 9: Create Pull Request on GitHub

1. Go to https://github.com/your-username/adf-python-pipeline
2. You'll see a notification: "Compare & pull request"
3. Click that button
4. Fill in the PR details:

**Title:**
```
Add Python-based Azure Data Factory Pipeline
```

**Description:**
```markdown
## Description
This pull request adds a complete Python-based ADF data pipeline for automated data processing.

## Changes
- ✅ Core data processing module (DataProcessor class)
- ✅ Pipeline orchestration framework
- ✅ Data cleaning and transformation logic
- ✅ Data validation framework
- ✅ Unit tests (8 test cases)
- ✅ Azure deployment guide
- ✅ Configuration management

## Features
- Reads CSV data from source
- Removes duplicates and handles missing values
- Normalizes and enriches data
- Validates data quality
- Writes processed output to CSV
- Comprehensive logging and error handling

## Testing
- All tests pass: `pytest tests/ -v`
- Manual testing with sample data successful
- Pipeline execution: ~2 seconds for 8 records

## How to Test
1. Run locally: `python src/pipeline_orchestrator.py`
2. Run tests: `python -m pytest tests/ -v`

## Type of Change
- [x] New feature
- [ ] Bug fix
- [ ] Documentation change

## Checklist
- [x] Code follows project style
- [x] Self-review completed
- [x] Tests added and passing
- [x] Documentation updated
- [x] No breaking changes
```

5. Click "Create pull request"

### ✅ STEP 10: Wait for Review & Feedback

After creating the PR:
1. Maintainers will review your code
2. They may ask for changes
3. Make requested changes and commit again
4. The PR will update automatically

### ✅ STEP 11: Merge (After Approval)

Once all reviewers approve:
1. Click "Merge pull request" button
2. Choose merge strategy (usually "Create a merge commit")
3. Click "Confirm merge"

**Congratulations! Your code is now part of the project!** 🎉

## What If They Ask for Changes?

**Scenario: Reviewer requests changes to your code**

1. Make the changes locally
2. Add and commit:
```bash
git add .
git commit -m "refactor: address PR review feedback"
```

3. Push to same branch:
```bash
git push origin feature/add-python-adf-pipeline
```

The PR automatically updates with your new changes!

## Common PR Mistakes to Avoid

❌ **Don't:**
- Commit to `main` branch directly
- Make huge commits with many unrelated changes
- Write vague commit messages ("fixed stuff")
- Forget to test before pushing
- Change unrelated code in your PR

✅ **Do:**
- Create feature branches
- Keep commits small and focused
- Write clear messages explaining "why"
- Test locally first
- Keep PR scope narrow

## Vocabulary You'll See

| Term | Meaning |
|------|---------|
| **Fork** | Create your own copy of a repository |
| **Clone** | Download repository to your computer |
| **Branch** | Separate version of code for your changes |
| **Commit** | Save changes with a message |
| **Push** | Send commits to GitHub |
| **Pull Request** | Propose your changes to be merged |
| **Merge** | Combine your changes into main code |
| **Reviewer** | Person who checks your code |

## Useful Git Commands

```bash
# Check current branch
git branch

# See what changed
git status

# View your commits
git log --oneline

# Undo last commit (before pushing)
git reset HEAD~1

# See changes before committing
git diff

# Switch branches
git checkout branch-name
```

## After Your First PR - Next Steps

1. ⭐ Ask another developer to review your PR (great learning!)
2. 📝 Add comments explaining complex logic
3. 🧪 Expand your tests
4. 🚀 Deploy to Azure using the AZURE_DEPLOYMENT_GUIDE.md
5. 📚 Read how to set up CI/CD pipelines

## Need Help?

- **GitHub Help**: https://docs.github.com/
- **Git Tutorial**: https://git-scm.com/book/en/v2
- **Our README**: [README.md](README.md)
- **Deployment Guide**: [AZURE_DEPLOYMENT_GUIDE.md](AZURE_DEPLOYMENT_GUIDE.md)

---

**You've got this! Creating your first pull request is a big step in your development journey.** 🚀

*Last Updated: February 18, 2026*
