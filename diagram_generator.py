import os
from graphviz import Digraph

class DiagramGenerator:
    def __init__(self, parsed_data, output_dir="generated_docs"):
        self.parsed_data = parsed_data
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate(self):
        dot = Digraph(comment="Code Structure", format='png')
        dot.attr(rankdir='TB', size='10')

        for item in self.parsed_data:
            node_id = item["name"]
            label = f"{item['type'].capitalize()}: {item['name']}"
            dot.node(node_id, label=label, shape="box")

            if item["type"] == "class":
                for method in item.get("methods", []):
                    method_id = f"{item['name']}.{method}"
                    dot.node(method_id, label=f"Method: {method}", shape="ellipse")
                    dot.edge(item["name"], method_id)

        output_path = os.path.join(self.output_dir, "structure_diagram")
        dot.render(output_path, cleanup=True)
        print(f"✅ Diagram saved at {output_path}.png")
