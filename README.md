# Regex Data Extraction & Secure Validation

## Overview
This project is a Python program that extracts structured data from raw text using
regular expressions. It simulates processing untrusted data returned from an external API.

## Extracted Data Types
- Email addresses
- URLs
- Phone numbers
- Credit card numbers

## Input
The input is a realistic text file (`sample_input.txt`) containing both valid and
invalid data formats.

## Output
The program outputs extracted data in a structured JSON format
(`sample_output.json`).

## Security Considerations
- Malformed data is ignored
- Only well-formed patterns are extracted
- Input is treated as untrusted

## How to Run
```bash
python data_extractor.py
