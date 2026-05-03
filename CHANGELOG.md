# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Released]

## [0.2.0] - 2026-05-04

### Added
- CSV-based recipient management (`data/contacts.csv`).
- HTML template personalisation with Jinja2 (`{{name}}` placeholders).
- Support for plain text along with HTML (MIME multipart/alternative).
- Configurable send delay between emails to avoid spam filters.
- Retry logic (up to 3 attempts) for failed sends.
- Delivery summary printed to console on completion.
- Full delivery log saved to `output/sent_log.csv`.
- Failed recipients saved to `output/failed_recipients.csv`.
- `--retry-failed` CLI flag to re-run only failed recipients.
- Secure credential loading via `python-dotenv`.
- Logging system with timestamped output.
- Package restructured for professional distribution (added `cli.py`, `__main__.py`).
- Added `email-sender` command-line entry point.
- Updated `pyproject.toml` with project dependencies.

### Changed
- Refactored email sending logic to handle multiple recipients in a single `send_email` call.
- Bulk email sending via Gmail SMTP.

## [0.1.0] - 2026-03-29

### Added
- Initial release of `email-sender-automation`.
- Basic automated email sending via Gmail SMTP.
