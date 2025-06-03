# Nexus Framework v2.3: Local Development Setup Guide

## Introduction

This guide provides step-by-step instructions for setting up a local development environment for the Nexus Framework v2.3. Following these instructions will ensure you have all the necessary tools, dependencies, and configurations to effectively develop and test the framework.

The setup process is designed to be platform-agnostic where possible, with specific instructions for Linux, macOS, and Windows with WSL2 where platform differences exist.

## Prerequisites

Before beginning the setup process, ensure you have:

- Administrative access to your development machine
- A GitHub account with access to the Nexus Framework repository
- Required API keys for external services (OpenAI, Anthropic, etc.)
- Sufficient disk space (at least 50GB free)
- A reliable internet connection

## Step 1: Development Environment Setup

### Installing Core Dependencies

#### Linux (Ubuntu/Debian)

```bash
# Update package lists
sudo apt update

# Install system dependencies
sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git

# Install Python 3.10
sudo apt install -y python3.10 python3.10-venv python3.10-dev python3-pip

# Install Node.js 18.x
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Install Rust (optional)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

#### macOS

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.10
brew install python@3.10

# Install Node.js 18.x
brew install node@18

# Install Rust (optional)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

#### Windows with WSL2

1. Install WSL2 following [Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install)
2. Install Ubuntu 22.04 from the Microsoft Store
3. Open Ubuntu and follow the Linux (Ubuntu/Debian) instructions above

### Installing Docker

#### Linux (Ubuntu/Debian)

```bash
# Remove old versions
sudo apt remove docker docker-engine docker.io containerd runc

# Install dependencies
sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Set up the stable repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Add your user to the docker group
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

#### macOS

```bash
# Install Docker Desktop
brew install --cask docker

# Start Docker Desktop
open /Applications/Docker.app
```

#### Windows with WSL2

1. Install Docker Desktop for Windows
2. Enable WSL2 integration in Docker Desktop settings
3. In WSL2 Ubuntu terminal, verify Docker works:
   ```bash
   docker --version
   ```

## Step 2: Nexus Framework Repository Setup

### Cloning the Repository

```bash
# Clone the repository
git clone https://github.com/your-organization/nexus-framework.git
cd nexus-framework

# Set up Git identity
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Setting Up Python Environment

```bash
# Create a virtual environment
python3.10 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate  # Windows

# Install development dependencies
pip install -e ".[dev]"
```

### Installing Node.js Dependencies (if applicable)

```bash
# Install Node.js dependencies
npm install
```

## Step 3: Database Setup

### Setting Up PostgreSQL

#### Using Docker (Recommended)

```bash
# Start PostgreSQL container
docker run --name nexus-postgres -e POSTGRES_PASSWORD=nexusdev -e POSTGRES_USER=nexusdev -e POSTGRES_DB=nexus -p 5432:5432 -d postgres:15

# Verify connection
docker exec -it nexus-postgres psql -U nexusdev -d nexus -c "SELECT version();"
```

#### Local Installation (Alternative)

Follow the [PostgreSQL installation guide](https://www.postgresql.org/download/) for your platform.

### Setting Up Redis

#### Using Docker (Recommended)

```bash
# Start Redis container
docker run --name nexus-redis -p 6379:6379 -d redis:7

# Verify connection
docker exec -it nexus-redis redis-cli ping
```

#### Local Installation (Alternative)

Follow the [Redis installation guide](https://redis.io/docs/getting-started/installation/) for your platform.

### Setting Up Vector Database

#### Using Docker (Recommended)

```bash
# Start Chroma container
docker run --name nexus-chroma -p 8000:8000 -d ghcr.io/chroma-core/chroma:0.4.15

# Verify connection
curl http://localhost:8000/api/v1/heartbeat
```

## Step 4: Configuration Setup

### Environment Variables

Create a `.env` file in the project root:

```bash
# Create .env file from template
cp .env.example .env

# Edit the .env file with your settings
nano .env  # or use your preferred editor
```

Example `.env` file content:

```
NEXUS_ENV=development
NEXUS_LOG_LEVEL=DEBUG
NEXUS_DATABASE_URL=postgresql://nexusdev:nexusdev@localhost:5432/nexus
NEXUS_REDIS_URL=redis://localhost:6379/0
NEXUS_VECTOR_DB_URL=http://localhost:8000
NEXUS_OPENAI_API_KEY=your_openai_api_key
NEXUS_ANTHROPIC_API_KEY=your_anthropic_api_key
```

### Configuration Files

```bash
# Create local configuration
cp config/environments/development.example.yaml config/environments/development.local.yaml

# Edit the configuration file
nano config/environments/development.local.yaml  # or use your preferred editor
```

## Step 5: Development Tools Setup

### Setting Up VS Code (Recommended)

1. Install [Visual Studio Code](https://code.visualstudio.com/)
2. Install recommended extensions:
   ```bash
   code --install-extension ms-python.python
   code --install-extension ms-python.vscode-pylance
   code --install-extension ms-python.black-formatter
   code --install-extension ms-python.isort
   code --install-extension charliermarsh.ruff
   code --install-extension ms-azuretools.vscode-docker
   code --install-extension redhat.vscode-yaml
   code --install-extension eamodio.gitlens
   code --install-extension github.vscode-pull-request-github
   code --install-extension yzhang.markdown-all-in-one
   ```
3. Open the project in VS Code:
   ```bash
   code .
   ```
4. Use the VS Code Python extension to select the virtual environment

### Setting Up PyCharm (Alternative)

1. Install [PyCharm Professional](https://www.jetbrains.com/pycharm/)
2. Open the project in PyCharm
3. Configure the Python interpreter to use the virtual environment
4. Install recommended plugins:
   - Mypy
   - Black
   - Ruff
   - Docker

## Step 6: Running the Framework

### Starting Required Services

```bash
# Start all required services using Docker Compose
docker-compose -f docker-compose.dev.yml up -d
```

### Running the API Server

```bash
# Activate the virtual environment (if not already activated)
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate  # Windows

# Run the API server
python -m nexus.api.server
```

### Running the CLI

```bash
# Run the CLI
python -m nexus.cli.main --help
```

## Step 7: Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run specific tests
pytest tests/unit/core/agents/

# Run tests with coverage
pytest --cov=nexus
```

### Code Formatting

```bash
# Format code with Black
black nexus tests

# Sort imports with isort
isort nexus tests

# Lint code with Ruff
ruff check nexus tests
```

### Type Checking

```bash
# Run type checking with Mypy
mypy nexus
```

### Building Documentation

```bash
# Build documentation
cd docs
mkdocs build

# Serve documentation locally
mkdocs serve
```

## Step 8: Debugging

### Debugging with VS Code

1. Open the project in VS Code
2. Set breakpoints in your code
3. Create a launch configuration in `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Python: Current File",
         "type": "python",
         "request": "launch",
         "program": "${file}",
         "console": "integratedTerminal",
         "justMyCode": false,
         "env": {
           "PYTHONPATH": "${workspaceFolder}"
         }
       },
       {
         "name": "Python: API Server",
         "type": "python",
         "request": "launch",
         "module": "nexus.api.server",
         "console": "integratedTerminal",
         "justMyCode": false,
         "env": {
           "PYTHONPATH": "${workspaceFolder}"
         }
       }
     ]
   }
   ```
4. Start debugging using the VS Code debug panel

### Debugging with PyCharm

1. Open the project in PyCharm
2. Set breakpoints in your code
3. Create a run configuration for the module or file you want to debug
4. Start debugging

## Step 9: CI/CD Integration

### Setting Up Pre-commit Hooks

```bash
# Install pre-commit
pip install pre-commit

# Install the git hook scripts
pre-commit install

# Run pre-commit on all files
pre-commit run --all-files
```

### Local GitHub Actions Testing

```bash
# Install Act for local GitHub Actions testing
curl -s https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Run GitHub Actions locally
act -j build
```

## Step 10: Troubleshooting

### Common Issues and Solutions

#### Database Connection Issues

```bash
# Check if PostgreSQL container is running
docker ps | grep postgres

# Restart PostgreSQL container if needed
docker restart nexus-postgres

# Check PostgreSQL logs
docker logs nexus-postgres
```

#### Redis Connection Issues

```bash
# Check if Redis container is running
docker ps | grep redis

# Restart Redis container if needed
docker restart nexus-redis

# Check Redis logs
docker logs nexus-redis
```

#### Python Environment Issues

```bash
# Recreate virtual environment
rm -rf .venv
python3.10 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

#### Docker Issues

```bash
# Check Docker service status
sudo systemctl status docker

# Restart Docker service
sudo systemctl restart docker
```

### Getting Help

If you encounter issues not covered in this guide:

1. Check the project documentation in the `docs/` directory
2. Search for similar issues in the GitHub repository
3. Ask for help in the `#nexus-help` Slack channel
4. Create a GitHub issue with detailed information about the problem

## Conclusion

You now have a fully configured local development environment for the Nexus Framework v2.3. This setup allows you to develop, test, and debug the framework effectively.

For more information on specific components or workflows, refer to the relevant documentation in the `docs/` directory.
