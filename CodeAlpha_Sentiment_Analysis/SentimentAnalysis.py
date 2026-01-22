import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

nltk.download('vader_lexicon')
data = {
    "Review": [
        "This product is amazing and works perfectly",
        "Very bad quality, totally disappointed",
        "Average product, nothing special",
        "Excellent performance and great value",
        "Worst experience ever, waste of money"
    ]
}

df = pd.DataFrame(data)
sia = SentimentIntensityAnalyzer()
def get_sentiment(text):
    score = sia.polarity_scores(text)["compound"]

    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"
df["Sentiment"] = df["Review"].apply(get_sentiment)
print(df)
df["Positive_Score"] = df["Review"].apply(lambda x: sia.polarity_scores(x)["pos"])
df["Negative_Score"] = df["Review"].apply(lambda x: sia.polarity_scores(x)["neg"])
df["Neutral_Score"]  = df["Review"].apply(lambda x: sia.polarity_scores(x)["neu"])
sentiment_counts = df["Sentiment"].value_counts()

plt.figure()
plt.bar(sentiment_counts.index, sentiment_counts.values)
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.show()
 