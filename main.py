from code_parser import CodeParser
from doc_generator import DocGenerator
from interactive_bot import DocumentationBot
from diagram_generator import DiagramGenerator
from version import __version__

def main():
    print(f"📦 MCP Documentation Bot - v{__version__}")
    repo_path = "example_project"  # Path to your codebase
    parser = CodeParser(repo_path)
    parsed_data = parser.parse()

    doc_gen = DocGenerator(parsed_data)
    doc_gen.generate_all()

    diagram_gen = DiagramGenerator(parsed_data)
    diagram_gen.generate()


    print("✅ Documentation generated in /generated_docs")

    # Move the bot call here to keep everything inside `main`
    bot = DocumentationBot(parsed_data)
    bot.start()

if __name__ == "__main__":
    main()
