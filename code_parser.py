import os
import ast

class CodeParser:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.parsed_data = []

    def parse(self):
        for dirpath, _, filenames in os.walk(self.repo_path):
            for filename in filenames:
                if filename.endswith(".py"):
                    file_path = os.path.join(dirpath, filename)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            source = f.read()
                            tree = ast.parse(source)
                            self._extract_from_ast(tree, file_path, source)
                    except Exception as e:
                        print(f"❌ Skipped {file_path}: {e}")
        return self.parsed_data

    def _extract_from_ast(self, tree, file_path, source):
        lines = source.split("\n")
        imports = self._extract_imports(tree)

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                args = [arg.arg for arg in node.args.args]
                docstring = ast.get_docstring(node)
                route = self._get_route_decorator(node)
                code_sample = self._extract_code_sample(node, lines)

                self.parsed_data.append({
                    "type": "function",
                    "name": node.name,
                    "args": args,
                    "docstring": docstring,
                    "file": file_path,
                    "route": route,
                    "imports": imports,
                    "code_sample": code_sample
                })

            elif isinstance(node, ast.ClassDef):
                methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                docstring = ast.get_docstring(node)
                code_sample = self._extract_code_sample(node, lines)

                self.parsed_data.append({
                    "type": "class",
                    "name": node.name,
                    "methods": methods,
                    "docstring": docstring,
                    "file": file_path,
                    "imports": imports,
                    "code_sample": code_sample
                })

    def _get_route_decorator(self, node):
        for decorator in getattr(node, 'decorator_list', []):
            if isinstance(decorator, ast.Call) and hasattr(decorator.func, 'attr'):
                if decorator.func.attr in {"get", "post", "put", "delete"}:
                    if decorator.args and isinstance(decorator.args[0], ast.Str):
                        return f"{decorator.func.attr.upper()} {decorator.args[0].s}"
        return None

    def _extract_imports(self, tree):
        imports = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports += [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                mod = node.module or ""
                imports += [f"{mod}.{alias.name}" for alias in node.names]
        return imports

    def _extract_code_sample(self, node, lines):
        try:
            start = node.lineno - 1
            end = getattr(node, 'end_lineno', start + 5)
            snippet = lines[start:end]
            return "\n".join(snippet).strip()
        except Exception:
            return None
