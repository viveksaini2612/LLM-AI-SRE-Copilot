from sentence_transformers import SentenceTransformer
import chromadb
import os

model = SentenceTransformer("all-MiniLM-L6-v2")
chroma = chromadb.Client()
collection = chroma.get_or_create_collection("sre-knowledge")

def load_docs(path="data"):
    docs = []
    for file in os.listdir(path):
        with open(os.path.join(path, file), "r") as f:
            docs.append(f.read())
    return docs

def embed_docs():
    docs = load_docs()
    embeddings = model.encode(docs).tolist()
    ids = [f"doc{i}" for i in range(len(docs))]
    collection.add(documents=docs, embeddings=embeddings, ids=ids)
    print("Embedded and stored in ChromaDB.")

