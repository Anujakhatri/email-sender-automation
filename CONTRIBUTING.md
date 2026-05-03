# Contributing to Email Sender Automation

Thank you for your interest in contributing! I welcome all types of contributions, from bug reports to new features.

---

## 🐛 Reporting Bugs

If you find a bug, please open an issue on GitHub and include:
- A clear, descriptive title.
- Steps to reproduce the bug.
- What you expected to happen vs. what actually happened.
- Your Python version and OS.

## 🛠️ Development Setup

Follow these steps to set up your local environment:

```bash
# 1. Clone the repo
git clone https://github.com/Anujakhatri/email-sender-automation.git
cd email-sender-automation

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install in editable mode with dev tools
pip install -e ".[dev]"

# 4. Set up your environment variables
cp .env.example .env
# Open .env and add your Gmail SMTP credentials
```

## 🧪 Running Tests

Always run tests before submitting a Pull Request to ensure everything works correctly:

```bash
# Run all tests
pytest tests/ -v

# Run tests with coverage report
pytest tests/ --cov=email_sender --cov-report=term-missing
```

## 📝 Code Style Guidelines

To keep the codebase clean and maintainable, please:
- Follow **PEP 8** standards.
- Keep functions small, focused, and well-named.
- Add **docstrings** to all public functions and classes.
- Ensure new features include corresponding **unit tests**.

## 🚀 Submitting a Pull Request

1. **Fork** the repository.
2. Create a **feature branch**: `git checkout -b feature/your-feature-name`.
3. **Commit** your changes: `git commit -m "feat: add your feature"`.
4. **Push** to your fork: `git push origin feature/your-feature-name`.
5. Open a **Pull Request** and describe your changes in detail.

## 💬 Commit Message Format

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` – A new feature
- `fix:` – A bug fix
- `docs:` – Documentation changes
- `chore:` – Tooling, config, or dependency updates
- `test:` – Adding or updating tests
