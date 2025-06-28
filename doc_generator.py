import os
import json
from version import __version__
class DocGenerator:
    def __init__(self, parsed_data, output_dir="generated_docs"):
        self.parsed_data = parsed_data
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_readme(self):
        content = (
            "# Project Documentation\n\n"
            "This documentation is auto-generated to help developers understand the structure and key components of the codebase.\n\n"
            "## \ud83d\udcc1 Contents\n"
            "- [API Documentation](API_DOCS.md)\n\n"
            "## \ud83d\ude80 Overview\n"
            "This tool analyzes a Python codebase and auto-generates:\n"
            "- Function and class documentation\n"
            "- API endpoint mappings (from FastAPI decorators)\n"
            "- Detected dependencies (`import`/`from` statements)\n"
            "- Markdown-formatted technical documentation\n\n"
            "## \u2699\ufe0f Setup Guide\n\n"
            "1. **Clone your target repo or place `.py` files into `example_project/`**  \n"
            "2. **Install Python 3.8+ and dependencies:**\n\n"
            "```bash\n"
            "pip install -r requirements.txt\n"
            "```\n\n"
            "3. **Run the bot:**\n\n"
            "```bash\n"
            "python main.py\n"
            "```\n\n"
            "4. **View generated files in:**\n\n"
            "```\n"
            "generated_docs/\n"
            "\u251c\u2500\u2500 README.md\n"
            "\u2514\u2500\u2500 API_DOCS.md\n"
            "```\n\n"
            "## 📊 Diagram\n"
            "![Structure Diagram](structure_diagram.png)\n\n"
            "## \ud83e\udde0 Sample Usage\n\n"
            "Assume this code inside `example_project/sample.py`:\n\n"
            "```python\n"
            "def greet(name):\n"
            "    \"\"\"Greets the user with their name.\"\"\"\n"
            "    return f\"Hello, {name}!\"\n"
            "```\n\n"
            "The tool will generate:\n\n"
            "```\n"
            "## Function: `greet`\n"
            "**File:** `example_project/sample.py`\n"
            "**Arguments:** name\n"
            "**Docstring:** Greets the user with their name.\n"
            "```\n\n"
            "## \ud83d\udccc Notes\n"
            "- API routes are detected for FastAPI-like decorators (e.g., `@app.get(\"/path\")`)\n"
            "- Dependencies are extracted per file and shown in **API_DOCS.md**\n"
            "- Files with syntax errors are skipped and printed in the terminal\n\n"
            "## \ud83d\udd0c Integration Guide\n"
            "To use this bot in your own project:\n\n"
            "1. Copy `code_parser.py`, `doc_generator.py`, and `interactive_bot.py` into your repo.\n"
            "2. Point `main.py` to your repo path:\n\n"
            "```python\n"
            "repo_path = \"your_codebase\"\n"
            "```\n\n"
            "## \ud83d\udee0\ufe0f Troubleshooting\n"
            "- If a file contains **syntax errors**, it will be skipped with an error shown in the terminal.\n"
            "- Make sure uploaded `.py` files are **UTF-8 encoded** to avoid parsing issues.\n"
            "- For API route detection to work, functions must use decorators like `@app.get(\"/route\")`\n"
            "- Ensure functions/classes have docstrings for better output\n\n"
            f"## 📌 Version\n"
            f"Current release: `v{__version__}`\n\n"
        )

        readme_path = os.path.join(self.output_dir, "README.md")
        with open(readme_path, "w", encoding="utf-8", errors="ignore") as f:
            f.write(content)

    def generate_api_docs(self):
        api_path = os.path.join(self.output_dir, "API_DOCS.md")
        best_practices = []

        with open(api_path, "w", encoding="utf-8") as f:
            f.write("# API Documentation\n\n")
            for item in self.parsed_data:
                f.write(f"## {item['type'].capitalize()}: `{item['name']}`\n")
                f.write(f"**File:** `{item['file']}`\n\n")

                if item["type"] == "function":
                    f.write(f"**Arguments:** {', '.join(item['args']) or 'None'}\n\n")
                    if item.get("route"):
                        f.write(f"**API Route:** `{item['route']}`\n\n")
                elif item["type"] == "class":
                    f.write(f"**Methods:** {', '.join(item['methods']) or 'None'}\n\n")

                if "imports" in item and item["imports"]:
                    f.write(f"**Dependencies:** `{', '.join(sorted(set(item['imports'])))}`\n\n")

                f.write("**Docstring:**\n\n")
                f.write(f"{item['docstring'] or 'No documentation provided.'}\n\n")

                if item.get("code_sample"):
                    f.write("**Code Example:**\n\n")
                    f.write("```python\n")
                    f.write(f"{item['code_sample'].strip()}\n")
                    f.write("```\n\n")

                if not item.get("docstring"):
                    best_practices.append({"issue": "Missing docstring", "item": item['name'], "file": item['file']})
                if item.get("code_sample") and len(item["code_sample"].splitlines()) > 20:
                    best_practices.append({"issue": "Method too long (>20 lines)", "item": item['name'], "file": item['file']})

                f.write("---\n\n")

        if best_practices:
            tips_path = os.path.join(self.output_dir, "BEST_PRACTICES.json")
            with open(tips_path, "w", encoding="utf-8") as bp:
                json.dump(best_practices, bp, indent=2)

    def generate_all(self):
        self.generate_readme()
        self.generate_api_docs()
