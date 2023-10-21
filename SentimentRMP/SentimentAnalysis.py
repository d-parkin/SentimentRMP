from google.cloud import language_v1
import os
import pandas as pd

# api credentials
credential_path = "C:\\Users\\parki\\Downloads\\sentimentrmp-07cccc3fa185.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def analyze_sentiment(text):
    # Initialize the Natural Language API client
    client = language_v1.LanguageServiceClient()

    # Create a document object with the text to analyze
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Analyze sentiment
    response = client.analyze_sentiment(request={'document': document})

    # Get sentiment score and magnitude
    sentiment = response.document_sentiment
    score = sentiment.score
    magnitude = sentiment.magnitude

    return score, magnitude

# Load csv and create new columns
df = pd.read_csv(r'C:\Users\parki\Downloads\SentimentRMP\SentimentRMP\rating.CSV')
df['Sentiment Score'] = None
df['Sentiment Magnitude'] = None

target_column = 'Review'

# Iterate through each row in the specified column and perform sentiment analysis
for index, row in df.iterrows():
    text = row[target_column]
    score, magnitude = analyze_sentiment(text)
    df.at[index, 'Sentiment Score'] = score
    df.at[index, 'Sentiment Magnitude'] = magnitude
    print(index)

# Save the DataFrame with sentiment analysis results to a new CSV file
df.to_csv('Ratings+Sentiment.csv', index=False)



