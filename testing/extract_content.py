import json
import re
import pypdf


with open("data/headings.json", "r") as file:
    headings = json.loads(file.read())

# Read the pdf file
with open("./data/ugrulebook.pdf", "rb") as file:
    pdf = pypdf.PdfReader(file)

    text = ""
    for page in pdf.pages[6:]:
        text += page.extract_text()

text = re.sub(r" +", r" ", text)
indexes = []
for heading in headings:
    start = text.find(heading[0])
    if start == -1:
        print("Unable to find: ", heading[0])
        continue
    indexes.append(start)

print(indexes)
docs = []
for i in range(len(indexes) - 1):
    docs.append(text[indexes[i] : indexes[i + 1]])

print(len(docs))
# with open("data/final.json", "w") as f:
#     f.write(json.dumps(docs))
