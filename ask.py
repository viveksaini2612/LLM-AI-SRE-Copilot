from rag import ask

print("SRE Copilot ready! Type your question or 'exit'")
while True:
    query = input("Q: ")
    if query.lower() in ('exit', 'quit'):
        break
    answer = ask(query)
    print(f"A: {answer}\n")
