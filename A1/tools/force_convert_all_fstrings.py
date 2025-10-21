import ast
from pathlib import Path

p = Path(
    r"d:\KJ\Personal_projects\_web_fun_builds\Kartavya_Business_Analytics2025\A1\pages\Experiment.py"
)
orig = p.read_text(encoding="utf-8")
backup = p.with_suffix(".py.fstrings.bak")
backup.write_text(orig, encoding="utf-8")


class ForceFStringTransformer(ast.NodeTransformer):
    def visit_JoinedStr(self, node):
        parts = []
        args = []
        for value in node.values:
            if isinstance(value, ast.Constant):
                # escape braces in literal parts
                part = (
                    value.value.replace("{", "{{").replace("}", "}}")
                    if isinstance(value.value, str)
                    else str(value.value)
                )
                parts.append(part)
            elif isinstance(value, ast.FormattedValue):
                # placeholder
                # include format spec if it's a simple constant
                if value.format_spec and isinstance(value.format_spec, ast.Constant):
                    parts.append("{:" + str(value.format_spec.value) + "}")
                else:
                    parts.append("{}")
                # append the expression source as an arg
                try:
                    expr_src = ast.unparse(value.value)
                except Exception:
                    # fallback: use repr of AST
                    expr_src = ast.dump(value.value)
                args.append(ast.parse(expr_src, mode="eval").body)
            else:
                # unknown part; fallback to stringification
                try:
                    txt = ast.unparse(value)
                except Exception:
                    txt = str(value)
                parts.append(txt)
        fmt_str = ast.Constant(value="".join(parts))
        if args:
            format_attr = ast.Attribute(value=fmt_str, attr="format", ctx=ast.Load())
            call = ast.Call(func=format_attr, args=args, keywords=[])
            return ast.copy_location(call, node)
        else:
            return ast.copy_location(fmt_str, node)


tree = ast.parse(orig)
new_tree = ForceFStringTransformer().visit(tree)
ast.fix_missing_locations(new_tree)
new_src = ast.unparse(new_tree)

if new_src != orig:
    p.write_text(new_src, encoding="utf-8")
    print(f"Converted all f-strings in {p}; backup saved as {backup}")
else:
    print("No changes were necessary.")
