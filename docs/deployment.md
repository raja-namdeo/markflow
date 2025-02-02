# MarkFlow Deployment Guide

> **Author**: Raja Namdeo  
> **Email**: cse.rajanamdeo@gmail.com  
> **Role**: Software Developer  

This guide explains how to deploy and maintain MarkFlow using free services.

## Quick Links

- GitHub Repository: [markflow](https://github.com/raja-namdeo/markflow)
- Documentation: [ReadTheDocs](https://app.readthedocs.org/dashboard/)
- Package: [PyPI](https://pypi.org/project/markflow/)
- Web Demo: [Streamlit](https://share.streamlit.io/raja-namdeo/markflow/main/web/streamlit_app.py)

## Services Overview

### 1. GitHub
- Code repository
- Version control
- Issue tracking
- Project management
- CI/CD with GitHub Actions
- Free static website hosting with GitHub Pages

### 2. ReadTheDocs
- Documentation hosting
- Automatic builds
- Version control
- Search functionality
- Free for open source

### 3. PyPI
- Package distribution
- Version management
- Free for open source

### 4. Web Demo (Streamlit)
- Interactive web demo
- Free hosting on Streamlit Cloud
- Real-time conversion

## Setup Instructions

### GitHub Repository Setup

1. Create new repository:
   ```bash
   # Initialize repository
   git init
   git add .
   git commit -m "Initial commit"
   
   # Create GitHub repository named 'markflow'
   # Then push code:
   git remote add origin https://github.com/yourusername/markflow.git
   git push -u origin main
   ```

2. Configure repository settings:
   - Enable Issues
   - Enable Projects
   - Enable Discussions
   - Enable GitHub Pages
   - Set branch protection rules

3. Add repository topics:
   - markdown
   - pdf
   - converter
   - python
   - documentation
   - gui
   - cli

### Private Repository Setup

GitHub offers private repositories with these features:
- Unlimited private repositories
- Access control
- Secret management
- Private issue tracking

To make files/directories private:
1. Create a separate private repository
2. Use Git submodules for private code
3. Use `.gitignore` for sensitive files
4. Use GitHub Secrets for tokens/keys

Example `.gitignore` for private files:
```gitignore
# Private files
private/
*.key
*.pem
config.private.yml

# Sensitive data
secrets/
credentials/
```

### ReadTheDocs Setup

1. Visit [ReadTheDocs](https://readthedocs.org/)
2. Connect GitHub account
3. Import repository
4. Configure webhook
5. Add `.readthedocs.yaml`:
   ```yaml
   version: 2
   
   build:
     os: ubuntu-22.04
     tools:
       python: "3.9"
   
   sphinx:
     configuration: docs/conf.py
   
   python:
     install:
       - requirements: docs/requirements.txt
   ```

### PyPI Setup

1. Create account on [PyPI](https://pypi.org/)
2. Generate API token
3. Add token to GitHub secrets
4. Configure `setup.py` and `pyproject.toml`
5. Test deployment:
   ```bash
   python -m build
   python -m twine upload dist/*
   ```

### Streamlit Web Demo Setup

1. Create `streamlit_app.py`:
   ```python
   import streamlit as st
   from markflow.core import convert_to_pdf
   
   st.title("MarkFlow Online")
   st.write("Convert Markdown to PDF online")
   
   markdown_text = st.text_area("Enter Markdown")
   if st.button("Convert"):
       pdf_bytes = convert_to_pdf(markdown_text)
       st.download_button("Download PDF", pdf_bytes)
   ```

2. Create `requirements.txt` for Streamlit:
   ```
   streamlit
   markflow
   ```

3. Deploy to Streamlit Cloud:
   - Connect GitHub repository
   - Select `streamlit_app.py`
   - Configure environment

## Maintenance Guide

### Version Control

1. Create version branches:
   ```bash
   git checkout -b v1.0.0
   git push origin v1.0.0
   ```

2. Tag releases:
   ```bash
   git tag -a v1.0.0 -m "First stable release"
   git push origin v1.0.0
   ```

### Documentation Updates

1. Build locally:
   ```bash
   cd docs
   make html
   ```

2. Preview:
   ```bash
   python -m http.server -d _build/html
   ```

### CI/CD Pipeline

1. Automated tests on push
2. Documentation builds
3. PyPI deployment on tags
4. Streamlit deployment on main

## Free Resources

### Development
- GitHub Codespaces: 60 hours/month
- GitHub Actions: 2000 minutes/month
- ReadTheDocs: Unlimited builds

### Hosting
- GitHub Pages: Unlimited
- Streamlit Cloud: Up to 3 apps
- PyPI: Unlimited packages

### Analytics
- GitHub Insights
- ReadTheDocs Analytics
- PyPI Download Stats

## Security

1. Branch Protection:
   - Require pull request reviews
   - Require status checks
   - No force push

2. Dependency Scanning:
   - Enable Dependabot
   - Regular security updates
   - Vulnerability alerts

3. Code Scanning:
   - Enable CodeQL
   - Regular security analysis
   - Automated fixes

## Community Building

1. Templates:
   - Issue templates
   - PR templates
   - Contributing guidelines
   - Code of conduct

2. Documentation:
   - Getting started guide
   - API reference
   - Examples
   - Tutorials

3. Community:
   - GitHub Discussions
   - Issue labels
   - Project boards
   - Milestone tracking

## Monitoring

1. GitHub:
   - Stars and forks
   - Issue response time
   - PR merge time

2. ReadTheDocs:
   - Page views
   - Documentation coverage
   - Build status

3. PyPI:
   - Download counts
   - Version adoption
   - Dependency tracking

## Support

1. Issue Management:
   - Bug reports
   - Feature requests
   - Questions
   - Documentation

2. Communication:
   - GitHub Discussions
   - Issue comments
   - PR reviews
   - Release notes
