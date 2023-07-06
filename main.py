import feedparser
import openai
import ssl
import random

RSS_FEED_URL = ""  # Replace with your RSS feed URL
openai.api_key = "" # Replace with your OpenAI API key

ssl._create_default_https_context = ssl._create_unverified_context

def get_headlines(feed_url):
    headlines = []
    feed = feedparser.parse(feed_url)

    for entry in feed.entries:
        headlines.append(entry.title)

    return headlines

def rephrase_sentence(sentence):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Rephrase the following sentence, make it short and headline-style, DO NOT rephrase sentences which meaning you do not fully understand, DO NOT use dot at the end of the rewritten sentence and remove '(VIDEO)' and '(FOTO)' text: \"{sentence}\"\n\nRewritten sentence:",
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

def main():
    headlines = get_headlines(RSS_FEED_URL)
    rephrased_headlines = []

    for headline in headlines:
        rephrased_headline = rephrase_sentence(headline)
        rephrased_headlines.append(rephrased_headline)

    random.shuffle(rephrased_headlines)

    for i in range(len(rephrased_headlines)):
        print(f"Rephrased: {rephrased_headlines[i]}")
        print()

if __name__ == "__main__":
    main()
