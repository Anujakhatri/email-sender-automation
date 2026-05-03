# Contributing to Email Sender Automation

Thank you for your interest in contributing! Here's how to get started.

## Development Setup

```bash
# 1. Clone the repo
git clone https://github.com/Anujakhatri/email-sender-automation.git
cd email-sender-automation

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install with dev dependencies
pip install -e ".[dev]"

# 4. Set up environment
cp .env.example .env
# Edit .env with your SMTP credentials
```

## Running Tests

```bash
pytest tests/ -v
pytest tests/ --cov=email_sender --cov-report=term-missing
```

## Code Style

- Follow PEP 8
- Keep functions small and focused
- Add docstrings to all public functions
- Write tests for new features

## Submitting a Pull Request

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request describing your changes

## Commit Message Format

Use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` – new feature
- `fix:` – bug fix
- `docs:` – documentation only
- `chore:` – tooling or config changes
- `test:` – adding or updating tests
