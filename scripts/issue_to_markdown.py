import os
import re
from datetime import date


def extract_section(body, name):
    pattern = rf"### {name}\s*\n(.*?)(?=\n### |$)"
    match = re.search(pattern, body or "", re.DOTALL)
    return match.group(1).strip() if match else ""


issue_title = os.getenv("ISSUE_TITLE", "Known Issue")
issue_body = os.getenv("ISSUE_BODY", "")
issue_number = os.getenv("ISSUE_NUMBER", "0")

category = extract_section(issue_body, "Categoria") or "outros"
category_folder = category.lower().replace(" ", "-")

fields = {
    "Categoria": category,
    "Ambiente": extract_section(issue_body, "Ambiente"),
    "Sintoma": extract_section(issue_body, "Sintoma"),
    "Mensagem de erro": extract_section(issue_body, "Mensagem de erro"),
    "Causa identificada": extract_section(issue_body, "Causa identificada"),
    "Solução aplicada": extract_section(issue_body, "Solução aplicada"),
    "Tags": extract_section(issue_body, "Tags"),
}

safe_title = re.sub(r"[^a-zA-Z0-9-]", "-", issue_title.lower())
filename = f"ISSUE-{issue_number}-{safe_title}.md"

content = f"# {issue_title}\n\n"
for key, value in fields.items():
    content += f"## {key}\n\n{value}\n\n"

content += f"## Data\n\n{date.today()}\n"

os.makedirs(f"docs/{category_folder}", exist_ok=True)

with open(f"docs/{category_folder}/{filename}", "w", encoding="utf-8") as file:
    file.write(content)
