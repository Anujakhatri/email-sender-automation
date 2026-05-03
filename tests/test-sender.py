"""
tests/test_sender.py

Tests for sender.send_email() and send_with_retry().
All SMTP connections are mocked — no real emails are sent.
"""

import smtplib
from unittest.mock import MagicMock, patch

import pytest

from email_sender.sender import send_email, send_with_retry


FAKE_CREDS = dict(
    sender_email="you@gmail.com",
    sender_password="app-password",
    smtp_host="smtp.gmail.com",
    smtp_port=587,
)


# ── send_email() ───────────────────────────────────────────────────────────────

@patch("email_sender.sender.smtplib.SMTP")
def test_send_to_explicit_recipient(mock_smtp_cls):
    """Passing a recipient sends to that address and returns True."""
    mock_server = MagicMock()
    mock_smtp_cls.return_value.__enter__.return_value = mock_server

    result = send_email(
        subject="Test",
        body="<p>Hello</p>",
        recipients="alice@example.com",
        **FAKE_CREDS,
    )

    assert result is True
    mock_server.starttls.assert_called_once()
    mock_server.login.assert_called_once_with("you@gmail.com", "app-password")
    mock_server.sendmail.assert_called_once()


@patch("email_sender.sender.smtplib.SMTP")
def test_send_defaults_to_self_when_no_recipient(mock_smtp_cls):
    """When recipients=None the email is sent to EMAIL_USER (yourself)."""
    mock_server = MagicMock()
    mock_smtp_cls.return_value.__enter__.return_value = mock_server

    send_email(subject="Test", body="<p>Hello</p>", **FAKE_CREDS)

    args = mock_server.sendmail.call_args[0]
    # to-address list should contain the sender (EMAIL_USER default)
    assert args[1] == "you@gmail.com" or args[1] == ["you@gmail.com"]


@patch("email_sender.sender.smtplib.SMTP")
def test_smtp_exception_returns_false(mock_smtp_cls):
    """A non-auth SMTP error returns False instead of raising."""
    mock_server = MagicMock()
    mock_smtp_cls.return_value.__enter__.return_value = mock_server
    mock_server.sendmail.side_effect = smtplib.SMTPException("timeout")

    result = send_email(
        subject="Test", body="<p>Hi</p>",
        recipients="alice@example.com", **FAKE_CREDS,
    )
    assert result is False


@patch("email_sender.sender.smtplib.SMTP")
def test_auth_error_propagates(mock_smtp_cls):
    """SMTPAuthenticationError must never be silently swallowed."""
    mock_server = MagicMock()
    mock_smtp_cls.return_value.__enter__.return_value = mock_server
    mock_server.login.side_effect = smtplib.SMTPAuthenticationError(535, b"Bad")

    with pytest.raises(smtplib.SMTPAuthenticationError):
        send_email(
            subject="Test", body="<p>Hi</p>",
            recipients="backupemail-for-test@gmail.com", **FAKE_CREDS,
        )


def test_missing_credentials_raises():
    """EnvironmentError raised if EMAIL_USER/EMAIL_PASS are both empty."""
    with pytest.raises(EnvironmentError, match="EMAIL_USER and EMAIL_PASS"):
        send_email(
            subject="Test", body="<p>Hi</p>",
            recipients="backupemail-for-test@gmail.com",
            sender_email="",
            sender_password="",
        )


# ── send_with_retry() ──────────────────────────────────────────────────────────

@patch("email_sender.sender.send_email", return_value=True)
def test_retry_succeeds_first_attempt(mock_send):
    ok, err = send_with_retry("Subject", "<p>Hi</p>", "alice@example.com", max_retries=3)
    assert ok is True
    assert err == ""
    assert mock_send.call_count == 1


@patch("email_sender.sender.time.sleep")
@patch("email_sender.sender.send_email", return_value=False)
def test_retry_exhausts_all_attempts(mock_send, mock_sleep):
    ok, err = send_with_retry("Subject", "<p>Hi</p>", "alice@example.com", max_retries=3)
    assert ok is False
    assert mock_send.call_count == 3


@patch("email_sender.sender.time.sleep")
@patch("email_sender.sender.send_email", side_effect=[False, False, True])
def test_retry_succeeds_on_third_attempt(mock_send, mock_sleep):
    ok, err = send_with_retry("Subject", "<p>Hi</p>", "alice@example.com", max_retries=3)
    assert ok is True
    assert mock_send.call_count == 3