"""
AST-based f-string converter placeholder.
This file was used during development to convert f-strings; it's now a harmless no-op.
"""


def main():
    print("ast_fstring_converter.py is a no-op placeholder.")


if __name__ == "__main__":
    main()
import ast
from pathlib import Path

p = Path(
    r"d:\KJ\Personal_projects\_web_fun_builds\Kartavya_Business_Analytics2025\A1\pages\Experiment.py"
)
orig = p.read_text(encoding="utf-8")
backup = p.with_suffix(".py.bak")
backup.write_text(orig, encoding="utf-8")


class FStringTransformer(ast.NodeTransformer):
    def visit_Constant(self, node):
        return node

    def visit_JoinedStr(self, node):
        # JoinedStr represents an f-string. It contains Constant and FormattedValue nodes.
        # If it has no FormattedValue (i.e., only Constant parts), convert to Constant string.
        # Else if all FormattedValue nodes are simple names or attributes without format spec,
        # convert to a .format() call: "... {} ...".format(name, attr)
        parts = []
        args = []
        can_convert_to_format = True
        for value in node.values:
            if isinstance(value, ast.Constant):
                parts.append(value.value.replace("{", "{{").replace("}", "}}"))
            elif isinstance(value, ast.FormattedValue):
                # Check if simple (Name or Attribute) and no conversion/format spec
                if (
                    isinstance(value.value, (ast.Name, ast.Attribute))
                    and value.conversion == -1
                    and (value.format_spec is None)
                ):
                    parts.append("{}")
                    # store source code for the value
                    # ast.get_source_segment is not reliable here; use ast.unparse
                    args.append(ast.unparse(value.value))
                else:
                    can_convert_to_format = False
                    break
            else:
                can_convert_to_format = False
                break
        if not node.values:
            return ast.Constant(value="")
        if can_convert_to_format:
            if args:
                # Build a Call node: Constant string .format(arg1, arg2)
                fmt_str = ast.Constant(value="".join(parts))
                format_attr = ast.Attribute(
                    value=fmt_str, attr="format", ctx=ast.Load()
                )
                call = ast.Call(
                    func=format_attr,
                    args=[ast.parse(a, mode="eval").body for a in args],
                    keywords=[],
                )
                return ast.copy_location(call, node)
            else:
                # No formatted values - just a constant string
                return ast.Constant(value="".join(parts))
        return node


tree = ast.parse(orig)
transformer = FStringTransformer()
new_tree = transformer.visit(tree)
ast.fix_missing_locations(new_tree)
new_src = ast.unparse(new_tree)

# Write back if changed
if new_src != orig:
    p.write_text(new_src, encoding="utf-8")
    print(f"Converted f-strings in {p}; backup saved as {backup}")
else:
    print("No changes made by AST converter.")
