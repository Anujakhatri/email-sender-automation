"""
tests/test_template_renderer.py

Tests for template_renderer.render_template() and preview_template().
Uses a temporary HTML file so no real data/template.html is needed.
"""

import pytest
from pathlib import Path

from email_sender.template_renderer import render_template, preview_template


SIMPLE_TEMPLATE = "<h1>Hello {{ name }}!</h1><p>Your email: {{ email }}</p>"


@pytest.fixture
def template_file(tmp_path: Path) -> Path:
    """Write a minimal Jinja2 template to a temp file and return its path."""
    t = tmp_path / "template.html"
    t.write_text(SIMPLE_TEMPLATE, encoding="utf-8")
    return t


def test_render_replaces_name(template_file: Path) -> None:
    result = render_template(
        {"name": "Alice", "email": "alice@example.com"},
        template_path=template_file,
    )
    assert "Alice" in result
    assert "alice@example.com" in result


def test_render_missing_variable_renders_empty(template_file: Path) -> None:
    """Jinja2 renders missing variables as empty string by default."""
    result = render_template({"email": "testemail@gmail.com"}, template_path=template_file)
    assert "Hello !" in result  # {{ name }} rendered as empty


def test_render_file_not_found_raises() -> None:
    with pytest.raises(FileNotFoundError, match="template not found"):
        render_template({"name": "Alice"}, template_path=Path("/nonexistent/template.html"))


def test_preview_returns_string(template_file: Path, monkeypatch) -> None:
    """preview_template() should return an HTML string without errors."""
    monkeypatch.setattr("email_sender.config.TEMPLATE_HTML", template_file)
    result = preview_template()
    assert isinstance(result, str)
    assert len(result) > 0


def test_preview_uses_sample_data(template_file: Path, monkeypatch) -> None:
    monkeypatch.setattr("email_sender.config.TEMPLATE_HTML", template_file)
    result = preview_template()
    assert "Sample Recipient" in result
