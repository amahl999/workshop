from transformers import pipeline

# Maak een sentimentanalyse-pipeline aan
sentiment_pipeline = pipeline("sentiment-analysis")

# Analyseer een tekst
result = sentiment_pipeline("I love using Hugging Face's Transformers library!")
print(result)