import os
from pathlib import Path
from jinja2 import Template

def render_template(context_or_template=None, context=None, template_path=None):
    # Support signature from tests and sender
    if isinstance(context_or_template, str):
        ctx = context or {}
    else:
        ctx = context_or_template or {}
        
    if template_path is not None:
        path = Path(template_path)
    else:
        from email_sender.config import TEMPLATE_HTML
        path = Path(TEMPLATE_HTML)
        
    if not path.exists():
        raise FileNotFoundError(f"template not found: {path}")
        
    template = Template(path.read_text(encoding="utf-8"))
    return template.render(**ctx)

def preview_template():
    return render_template({"name": "Sample Recipient", "email": "sample@example.com", "company": "Sample Corp"})
