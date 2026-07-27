import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download("vader_lexicon")

# Initialize analyzer
sia = SentimentIntensityAnalyzer()

# Sample reviews
reviews = [
    "This product is amazing! I really loved it.",
    "The quality is okay, nothing special.",
    "Very disappointed. It stopped working after two days.",
    "Excellent customer service and fast delivery.",
    "The product is average."
]

results = []

for review in reviews:
    score = sia.polarity_scores(review)

    if score["compound"] >= 0.05:
        sentiment = "Positive"
    elif score["compound"] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    results.append({
        "Review": review,
        "Sentiment": sentiment,
        "Compound Score": score["compound"]
    })

# Create DataFrame
df = pd.DataFrame(results)

# Print results
print(df)

# Save results
df.to_csv("sentiment_results.csv", index=False)

print("\nResults saved successfully as sentiment_results.csv")