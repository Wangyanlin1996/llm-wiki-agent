#!/usr/bin/env python3
"""
Convert a Markdown file to HTML for email rendering.

Usage:
    python tools/md2html.py <input.md> [-o output.html]

If -o is omitted, writes to stdout.
"""

import argparse
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    print("ERROR: markdown package not installed. Run: pip install markdown", file=sys.stderr)
    sys.exit(1)


def convert(md_text: str) -> str:
    """Convert markdown to styled HTML suitable for email."""
    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "nl2br"],
    )
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{ font-family: -apple-system, 'Segoe UI', Roboto, sans-serif; font-size: 14px; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 16px; }}
  h1 {{ font-size: 20px; border-bottom: 2px solid #eee; padding-bottom: 8px; }}
  h2 {{ font-size: 16px; margin-top: 24px; }}
  table {{ border-collapse: collapse; width: 100%; margin: 12px 0; }}
  th, td {{ border: 1px solid #ddd; padding: 6px 10px; text-align: left; }}
  th {{ background-color: #f5f5f5; }}
  code {{ background-color: #f5f5f5; padding: 2px 4px; border-radius: 3px; font-size: 13px; }}
  blockquote {{ border-left: 4px solid #ddd; margin: 0; padding: 4px 16px; color: #666; }}
  a {{ color: #0366d6; }}
</style>
</head>
<body>
{html_body}
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML for email")
    parser.add_argument("input", help="Input .md file path")
    parser.add_argument("-o", "--output", help="Output .html file path (default: stdout)")
    args = parser.parse_args()

    md_text = Path(args.input).read_text(encoding="utf-8")
    html = convert(md_text)

    if args.output:
        Path(args.output).write_text(html, encoding="utf-8")
        print(f"Written to {args.output}")
    else:
        print(html)


if __name__ == "__main__":
    main()
