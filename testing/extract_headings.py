import json
from dataclasses import dataclass
import pypdf
import re
from rich.progress import track


@dataclass()
class Heading:
    idx: str
    text: str


# Read the pdf file
with open("./data/ugrulebook.pdf", "rb") as file:
    pdf = pypdf.PdfReader(file)

    text = ""
    for page in pdf.pages[2:6]:
        text += page.extract_text()

headings = []
for line in text.splitlines()[5:]:
    line = line.strip()
    if line == "":
        continue
    if re.search(r"^\d", line) is None:
        if headings[-1][-1] == "-":
            headings[-1] = headings[-1][:-1] + line
        else:
            headings[-1] += " " + line
    else:
        headings.append(line)

headings = [re.findall(r"(.+)\s+\d+", heading)[0] for heading in headings]

for i in range(len(headings)):
    matches = re.findall(r"^([0-9.]+)\s+(.+)$", headings[i])[0]
    # headings[i] = Heading(matches[0], matches[1].strip())
    headings[i] = (matches[0], matches[1].strip())

with open("data/headings.json", "w") as f:
    f.write(json.dumps(headings))

# text = ""
# for page in track(pdf.pages[7:], description="Processing pdf pages"):
#     text += page.extract_text()[2:]

# with open("extracted.txt", "w") as f:
#     f.write(text)
