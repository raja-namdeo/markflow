# Managing Private Files in MarkFlow

> **Author**: Raja Namdeo  
> **Email**: cse.rajanamdeo@gmail.com  
> **Role**: Software Developer  

This guide explains how to manage private files in the MarkFlow project.

## Private Files Strategy

### 1. Using .gitignore

Create or update `.gitignore`:
```gitignore
# Private directories
private/
secrets/
credentials/

# Private files
*.key
*.pem
*.private.yml
*.private.json

# Environment files
.env
.env.local
.env.*.local

# IDE files
.idea/
.vscode/
*.swp
```

### 2. Using Git Submodules

For private code that needs version control:

1. Create a private repository:
   ```bash
   # Create private repo on GitHub: markflow-private
   
   # Initialize local private repo
   mkdir markflow-private
   cd markflow-private
   git init
   git remote add origin https://github.com/raja-namdeo/markflow-private.git
   ```

2. Add as submodule:
   ```bash
   # In main markflow repository
   git submodule add https://github.com/raja-namdeo/markflow-private.git private
   ```

3. Update .gitignore:
   ```gitignore
   # Ignore private directory contents but keep .gitmodules
   private/*
   !private/.gitkeep
   ```

### 3. Using GitHub Secrets

For sensitive data like API keys:

1. Go to GitHub repository settings
2. Navigate to Secrets and Variables > Actions
3. Add new repository secret:
   - PYPI_API_TOKEN
   - READTHEDOCS_TOKEN
   - etc.

### 4. Using Environment Variables

For local development:

1. Create `.env` file:
   ```bash
   # .env
   PYPI_API_TOKEN=your_token_here
   PRIVATE_KEY=your_key_here
   ```

2. Add to .gitignore:
   ```gitignore
   .env
   ```

3. Load in code:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

## Private Files Examples

### Configuration Files
```yaml
# config.private.yml
api_key: "your_api_key"
secret_token: "your_token"
private_endpoint: "https://api.example.com"
```

### Credentials
```json
// credentials.private.json
{
  "username": "your_username",
  "password": "your_password",
  "api_keys": {
    "service1": "key1",
    "service2": "key2"
  }
}
```

### Private Code
```python
# private/sensitive_operations.py
def process_private_data():
    # Private implementation
    pass
```

## Best Practices

1. **Never Commit Sensitive Data**
   - Use environment variables
   - Use GitHub secrets
   - Use private submodules

2. **Access Control**
   - Limit access to private repositories
   - Use branch protection
   - Enable 2FA

3. **Security**
   - Rotate secrets regularly
   - Audit access logs
   - Monitor dependencies

4. **Documentation**
   - Document private file locations
   - Maintain setup guides
   - Keep security policies updated

## Setup Instructions

1. **Initial Setup**
   ```bash
   # Clone main repository
   git clone https://github.com/raja-namdeo/markflow.git
   cd markflow
   
   # Clone private repository (if needed)
   git submodule add https://github.com/raja-namdeo/markflow-private.git private
   
   # Create environment file
   cp .env.example .env
   ```

2. **Environment Configuration**
   ```bash
   # Edit .env file with your values
   nano .env
   ```

3. **Private Repository Access**
   ```bash
   # Add collaborators to private repository
   # GitHub > Settings > Collaborators > Add people
   ```

## Security Notes

1. **Token Security**
   - Never share tokens
   - Use environment variables
   - Rotate regularly

2. **Access Management**
   - Review access quarterly
   - Remove unused access
   - Document access changes

3. **Monitoring**
   - Check access logs
   - Monitor usage
   - Review security alerts
