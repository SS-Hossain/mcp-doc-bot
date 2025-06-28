import json
import os

class DocumentationBot:
    def __init__(self, parsed_data, log_json_path="logs/conversation_log.json", log_txt_path="logs/conversation_log.txt"):
        self.parsed_data = parsed_data
        self.log_json_path = log_json_path
        self.log_txt_path = log_txt_path
        os.makedirs(os.path.dirname(log_json_path), exist_ok=True)

    def start(self):
        print("🤖 Welcome to the Developer Documentation Assistant!")
        print("Type a function/class name to get documentation, or type 'exit' to quit.\n")

        while True:
            query = input("🔍 Search: ").strip()
            if query.lower() == "exit":
                print("👋 Goodbye!")
                break

            results = [item for item in self.parsed_data if item["name"].lower() == query.lower()]

            if not results:
                print("⚠️ No match found. Try another name.\n")
                self._log_json(query, "No match found.")
            else:
                for item in results:
                    self._display_result(item)
                    self._log_json(query, item)
                    self._log_txt(item)

    def _display_result(self, item):
        print(f"\n📄 Type: {item['type'].capitalize()}")
        print(f"🔹 Name: {item['name']}")
        print(f"📁 File: {item['file']}")

        if item["type"] == "function":
            print(f"📌 Arguments: {', '.join(item.get('args', [])) or 'None'}")
            if item.get("route"):
                print(f"🔗 API Route: {item['route']}")

        elif item["type"] == "class":
            print(f"📌 Methods: {', '.join(item.get('methods', [])) or 'None'}")

        if item.get("imports"):
            print(f"📦 Dependencies: {', '.join(set(item['imports']))}")

        print(f"📝 Docstring:\n{item['docstring'] or 'No docstring provided.'}")
        print("-" * 50)

    def _log_json(self, query, result):
        entry = {
            "query": query,
            "response": result if isinstance(result, str) else {
                "type": result["type"],
                "name": result["name"],
                "file": result["file"]
            }
        }

        try:
            if os.path.exists(self.log_json_path):
                with open(self.log_json_path, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            else:
                logs = []

            logs.append(entry)

            with open(self.log_json_path, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2)

        except Exception as e:
            print(f"⚠️ Failed to write JSON log: {e}")

    def _log_txt(self, item):
        try:
            with open(self.log_txt_path, "a", encoding="utf-8") as f:
                line = f"{item['name']} -> {item['type']} {item['name']} from {item['file']}\n"
                f.write(line)
        except Exception as e:
            print(f"⚠️ Failed to write TXT log: {e}")
