import ollama
from newspaper import Article

model = "llama3.2"

print("Starting Summary...")

article = Article("https://learn.microsoft.com/en-us/azure/well-architected/security/principles")
article.download()
article.parse()
#print(article.text)

systemPrompt = "Create a concise summary of Azure principles, make sure to highlight the key points."
prompt = article.text

output = ollama.generate(
            model=model, 
            prompt=prompt, 
            stream=False,
            system=systemPrompt,
            options={"temperature": 0.5}
)

print(output["response"])

print(output["context"])