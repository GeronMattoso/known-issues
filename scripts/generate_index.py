import os
from datetime import date

ROOT = "docs"
OUTPUT = os.path.join(ROOT, "index.md")

rows = []

for path, _, files in os.walk(ROOT):
    for file in files:
        if file.endswith(".md") and file != "index.md":
            full_path = os.path.join(path, file)
            relative = full_path.replace(ROOT + "/", "")
            title = file.replace(".md", "").replace("-", " ")
            category = path.replace(ROOT + "/", "")
            rows.append((file, title, category, relative))

rows.sort()

content = "# Base de Conhecimento\n\n"
content += f"Atualizado em: {date.today()}\n\n"
content += "| ID | Problema | Categoria | Documento |\n"
content += "|---|---|---|---|\n"

for item, title, category, relative in rows:
    content += f"| {item.split('-')[0]} | {title} | {category} | [{item}]({relative}) |\n"

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(content)
