import ollama

#prompt = "what is the city of Detroit best known for?";

prompt = "what are some popular things to do in Detroit?";

output = ollama.generate(model="llama3.2", prompt=prompt)

print(output["response"])