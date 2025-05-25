from sentence_transformers import SentenceTransformer
import chromadb
import subprocess

# Load the embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB and get/create the collection
chroma = chromadb.PersistentClient(path="./index")
collection = chroma.get_or_create_collection("sre-knowledge")

def ask(question):
    # Embed the question
    q_embed = embed_model.encode([question]).tolist()
    
    # Query the vector DB for top 3 relevant docs
    results = collection.query(query_embeddings=q_embed, n_results=3)
    
    # Join the retrieved docs as context
    context = "\n".join([doc for doc in results['documents'][0]])
    
    # Build prompt for LLM
    prompt = f"""
You are an SRE assistant. Use the context below to answer the question.

Context:
{context}

Question: {question}
Answer:
"""
    # Run the TinyLLaMA model locally via Ollama with the prompt
    result = subprocess.run(
        ["ollama", "run", "tinyllama"],
        input=prompt.encode(),
        capture_output=True
    )
    
    # Decode and return the answer text
    answer = result.stdout.decode()
    return answer.strip()
