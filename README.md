# 📄 MCP Documentation Bot

**MCP Documentation Bot** is an intelligent assistant that automatically parses Python codebases, generates developer-friendly documentation (like README and API docs), visualizes code structure with diagrams, and answers user queries through an interactive bot or Streamlit UI.

---

## 🚀 Features

### 🔍 Code Analysis
- Full repository scanning
- Function and class documentation extraction
- API endpoint detection (`FastAPI` route parsing)
- Dependency tracking (imports, method calls)

### 📚 Documentation Generation
- `README.md` with version and usage info
- `API_DOCS.md` with detailed function/class docs
- Setup guides and code examples
- Automatically generated structure diagram (`structure_diagram.png`)

### 💬 Interactive Help
- **CLI Bot**: Run `python main.py` to ask about code from terminal
- **Streamlit UI**: Upload files and interact visually
- Usage examples, best practice feedback, and troubleshooting info

### ✅ Best Practices
- Heuristic-based analysis to detect missing docstrings or bad practices
- JSON-based feedback for improvements

### 🎁 Bonus Features
- 📊 **Diagram Generation** (Flowchart of code structure)
- 🔖 **Version Tracking** (Auto-included in README)

---

## 🧪 Example Output

- `generated_docs/API_DOCS.md`
- `generated_docs/README.md`
- `generated_docs/structure_diagram.png`
- `logs/conversation_log.json`

---

## 🖥️ Streamlit App

```bash
streamlit run app.py
```

- Upload your `.py` files from the sidebar
- View auto-generated docs
- Ask the bot questions about your codebase
- Visualize and download the structure diagram

---

## 🖱️ CLI Bot

```bash
python main.py
```

- Type function or class names to get instant documentation
- Type `exit` to close the CLI assistant
- Logs are saved in `logs/conversation_log.txt` and `.json`

---

## 🧠 How It Works

1. Parses the AST (Abstract Syntax Tree) of Python files
2. Extracts metadata (name, args, docstrings, decorators)
3. Generates Markdown documentation
4. Builds an interactive Q&A system from parsed data
5. Optionally generates a class-function-method diagram

---

## 📦 Installation

```bash
git clone https://github.com/SS-Hossain/mcp-doc-bot.git
cd mcp-doc-bot
pip install -r requirements.txt
```

---

## 🛠️ Tech Stack

- Python 3.8+
- Streamlit
- AST module
- Graphviz (for diagram generation)
- JSON, Markdown, OS libraries

---

## 📁 Folder Structure

```
mcp-doc-bot/
├── example_project/             # Sample code to test
├── generated_docs/              # Output docs + diagram
├── logs/                        # Bot conversation logs
├── uploaded_project/            # Uploaded files via Streamlit
├── app.py                       # Streamlit UI
├── main.py                      # CLI assistant
├── code_parser.py               # AST-based parser
├── doc_generator.py             # README + API docs
├── diagram_generator.py         # Structure diagram
├── interactive_bot.py           # Terminal Q&A bot
├── version.py                   # Version control
└── requirements.txt
```

---

## 📌 Version
Current release: `v1.0.0`

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open issues or suggest features.

---

## 👨‍💻 Author

Made with ❤️ by [SK Shaid Hossain](https://github.com/SS-Hossain)
