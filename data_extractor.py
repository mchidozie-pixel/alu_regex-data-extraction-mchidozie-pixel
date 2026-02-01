import re
import json

# Read input text from file
with open("sample_input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Regex patterns
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
url_pattern = re.compile(r'https?://[^\s]+')
phone_pattern = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b')
credit_card_pattern = re.compile(r'\b(?:\d{4}[- ]?){3}\d{4}\b')

# Extract data
results = {
    "emails": email_pattern.findall(text),
    "urls": url_pattern.findall(text),
    "phones": phone_pattern.findall(text),
    "credit_cards": credit_card_pattern.findall(text)
}

# Save output to JSON file
with open("sample_output.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4)

# Print results
print(json.dumps(results, indent=4))
