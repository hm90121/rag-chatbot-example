import re
import json
from pathlib import Path
from pypdf import PdfReader

from rich.progress import track
from rich import print
from rich.prompt import Prompt

rulebook_path = Prompt.ask(
    "Enter path of the 'UG Rulebook' PDF file", default="./data/ugrulebook.pdf"
)
rulebook_path = Path(rulebook_path)
if not rulebook_path.exists() or not rulebook_path.is_file():
    print("[red]The specified file either does not exist or is not a file!")
    exit(1)
extracted_text_path = Prompt.ask(
    "Enter path where you want to store the extracted text", default="./data"
)
extracted_text_path = Path(extracted_text_path)
if not extracted_text_path.is_dir():
    print("[red]The specified path either does not exist or is not a directory!")
    exit(1)
extracted_text_path = extracted_text_path.joinpath("extracted.json")

reader = PdfReader(rulebook_path)
pages = reader.pages[7:]

contents = "\n".join([page.extract_text() for page in pages])

bold_texts = []


def visit_body(text, cm, tm, font_dict, font_size):
    if (
        len(text.strip()) > 0
        and font_dict is not None
        and font_dict["/BaseFont"] == "/CIDFont+F2"
    ):
        bold_texts.append(text)


for page in track(pages, description="Extracting text from PDF"):
    page.extract_text(visitor_text=visit_body)

headings = []
start_indexes = []
regex = re.compile(r"^\d.+$")
for text in track(bold_texts, description="Cleaning extracted text"):
    if re.search(regex, text) is not None:
        headings.append(text)
        start_indexes.append(contents.find(text))

docs = {}
for i in track(
    range(len(start_indexes) - 1),
    description="Retreiving useful content from extracted text",
):
    start = start_indexes[i]
    end = start_indexes[i + 1]
    docs[headings[i]] = contents[start:end]

print(f"Writing extracted text to [bold]'{str(extracted_text_path)}'")
with open(extracted_text_path, "w") as file:
    json.dump(docs, file)
