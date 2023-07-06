# RSS Headline Rephraser

This Python script fetches news headlines from an RSS feed, rephrases them using the OpenAI GPT-3.5 model, and shuffles the rephrased headlines. The purpose is to generate alternative versions of the news headlines while preserving their meaning.

## Usage

1. Install the required dependencies:

```
pip install feedparser
pip install openai
```

2. Set up the necessary variables:
- Set the `RSS_FEED_URL` variable to the URL of your desired RSS feed.
- Assign your OpenAI API key to the `openai.api_key` variable.

3. Run the script:

```
python main.py
```

4. The script will fetch the headlines from the specified RSS feed, rephrase them using the OpenAI GPT-3.5 model, shuffle the rephrased headlines, and display the results.

## Notes

- The rephrased headlines are limited to 50 tokens in length and are shuffled for variety.
- The script ignores SSL verification due to potential SSL certificate issues.
