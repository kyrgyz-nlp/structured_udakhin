# Make sure prodigy.json has appropriate environment variables
python scripts/mkconfig.py

# Small bit of code that downloads data, can be replaced with proper script
# that fetches data from s3 or another storage source.
wget https://raw.githubusercontent.com/explosion/prodigy-recipes/master/example-datasets/news_headlines.jsonl

# Show the stats, just for the logs
python -m prodigy stats

# Start Prodigy
python -m prodigy ner.manual nyt blank:en news_headlines.jsonl --label "COMPANY,PERSON"