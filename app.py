import streamlit as st
import os
import shutil
import json
from code_parser import CodeParser
from doc_generator import DocGenerator
from diagram_generator import DiagramGenerator
from version import __version__

# Initial config
st.set_page_config(page_title="MCP Doc Bot", layout="wide")
st.title("📄 MCP Documentation Bot")

# File upload
st.sidebar.header("🔍 Select Python Project")
uploaded_files = st.sidebar.file_uploader("Upload your .py files", type="py", accept_multiple_files=True)
st.sidebar.markdown(f"---\n**Version:** `{__version__}`")


if uploaded_files:
    # Clear old folder
    if os.path.exists("uploaded_project"):
        shutil.rmtree("uploaded_project")
    os.makedirs("uploaded_project", exist_ok=True)

    for file in uploaded_files:
        file_path = os.path.join("uploaded_project", file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())

# Generate docs
if st.sidebar.button("🛠️ Generate Docs"):
    parser = CodeParser("uploaded_project")
    parsed_data = parser.parse()

    # Generate docs
    doc_gen = DocGenerator(parsed_data)
    doc_gen.generate_all()

    # Generate diagram
    diagram = DiagramGenerator(parsed_data)
    diagram.generate()

    st.success("✅ Documentation generated!")

    # Preview API_DOCS
    st.markdown("### 📘 API_DOCS.md")
    with open("generated_docs/API_DOCS.md", "r", encoding="utf-8") as f:
        st.code(f.read(), language="markdown")

    # Preview README
    st.markdown("### 📕 README.md")
    with open("generated_docs/README.md", "r", encoding="utf-8") as f:
        st.code(f.read(), language="markdown")

    # Structured diagram with download
    structured_path = "generated_docs/structure_diagram.png"
    if os.path.exists(structured_path):
        st.markdown("### 📊 Structured Diagram")
        st.image(structured_path, caption="Structure Diagram", use_container_width=True)
        with open(structured_path, "rb") as f:
            st.download_button("📥 Download Diagram", f, file_name="structure_diagram.png", mime="image/png")

    # Best practices preview
    best_path = "generated_docs/BEST_PRACTICES.json"
    if os.path.exists(best_path):
        st.markdown("### ✅ Best Practices Feedback")
        with open(best_path, "r", encoding="utf-8") as f:
            feedback = json.load(f)
        for fb in feedback:
            st.markdown(f"- 🔍 **{fb['file']}** → `{fb['issue']}`")

    st.session_state["parsed_data"] = parsed_data

# Ask the Bot
st.markdown("## 🤖 Ask the Bot")
user_query = st.text_input("Enter function/class name to get docs:")

if user_query and "parsed_data" in st.session_state:
    parsed_data = st.session_state["parsed_data"]
    results = [item for item in parsed_data if item["name"].lower() == user_query.lower()]

    if not results:
        st.warning("No match found.")
        log_entry = {"query": user_query, "response": "No match found."}
    else:
        for item in results:
            st.markdown(f"### 📄 {item['type'].capitalize()}: `{item['name']}`")
            st.markdown(f"**File:** `{item['file']}`")

            if item["type"] == "function":
                st.markdown(f"**Arguments:** {', '.join(item.get('args', [])) or 'None'}")
                if item.get("route"):
                    st.markdown(f"**API Route:** `{item['route']}`")
            elif item["type"] == "class":
                st.markdown(f"**Methods:** {', '.join(item.get('methods', [])) or 'None'}")

            if item.get("imports"):
                st.markdown(f"**Dependencies:** `{', '.join(set(item['imports']))}`")

            st.markdown(f"**Docstring:**\n\n{item['docstring'] or 'No docstring provided.'}")

            log_entry = {
                "query": user_query,
                "response": {
                    "type": item["type"],
                    "name": item["name"],
                    "file": item["file"]
                }
            }

    # Save log
    try:
        os.makedirs("logs", exist_ok=True)
        log_path = "logs/conversation_log.json"
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as f:
                existing_logs = json.load(f)
        else:
            existing_logs = []

        existing_logs.append(log_entry)

        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(existing_logs, f, indent=2)

    except Exception as e:
        st.error(f"Failed to save conversation log: {e}")
