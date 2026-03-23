import json

with open('assignment2.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        for j, line in enumerate(cell['source']):
            stripped = line.lstrip(' ')
            indent = len(line) - len(stripped)
            if indent > 0 and indent % 4 != 0:
                print(f"Suspicious indentation in Cell {i}, Line {j+1}:")
                print(f"Line content: {repr(line)}")
                print(f"Indent level: {indent}")
