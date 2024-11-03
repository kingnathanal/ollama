import ollama
from newspaper import Article

model = "llama3.2"

print("Starting Summary...")

# Summarize articles about the pillars of the Azure Well-Architected Framework
articles = [
    "https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles",
    "https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/principles",
    "https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/principles",
    "https://learn.microsoft.com/en-us/azure/well-architected/security/principles",
    "https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/principles"
]
combined_text = ""
context = []
for article_url in articles:
    article = Article(article_url)
    article.download()
    article.parse()
    output = ollama.generate(
        model=model,
        prompt=article.text,
        stream=False,
        system="Create a concise summary of the article, highlighting the key points.",
        options={"temperature": 0.5},
        context=context
    )

systemPrompt = "Create a detailed summary of these articles, describing the key principles of the Azure Well-Architected Framework."
prompt = "Create me a summary about the key principles of the Azure Well-Architected Framework."

output = ollama.generate(
            model=model, 
            prompt=prompt, 
            stream=False,
            system=systemPrompt,
            options={"temperature": 1},
            context=context
)

print(output["response"])