from pathlib import Path
import json

from rich import print
from rich.prompt import Prompt

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA

# Ask user for path to extracted data file
extracted_text_path = Prompt.ask(
    "Enter the path to the file in which the extracted text is stored",
    default="./data/extracted.json",
)
extracted_text_path = Path(extracted_text_path)
if not extracted_text_path.is_file():
    print("[red]The specified path either does not exist or is not a file!")
    exit(1)

# Load data from file
with open(extracted_text_path, "r") as file:
    data = json.load(file)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create metadata for creating embeddings
texts = []
metadatas = []
for key, value in data.items():
    metadatas.append({"heading": key})
    texts.append(value)
retriever = Chroma.from_texts(
    texts=texts, embedding=embeddings, metadatas=metadatas
).as_retriever(search_kwargs={"k": 3})

# Create llm model for querying
llm = HuggingFacePipeline.from_model_id(
    model_id="bigscience/bloom-560m",
    task="text-generation"
)

# Join everything together using a chain
chain = RetrievalQA.from_llm(llm=llm, retriever=retriever)

while True:
    query = input("Enter your prompt (q for quitting): ")
    query = query.strip()

    if query == "q" or query == "quit":
        break
    if query == "":
        continue

    try:
        print(chain.run({"query": query}))
    except Exception as e:
        print(e)
    print("\n---\n")
