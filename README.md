# Secure Data Extraction Tool

This program extracts structured information (Emails, URLs, Phone Numbers, Currency, and Time) from raw text files. It is designed with safety in mind to handle real-world "messy" data and potential security threats.

## Features

- **Email Extraction**: Captures standard and complex email formats, with automatic masking for privacy.
- **URL Extraction**: Safely identifies web links.
- **Phone Number Parsing**: Handles various formats like `(123) 456-7890` or `123.456.7890`.
- **Currency Detection**: Identifies US dollar amounts with proper comma and decimal handling.
- **Time Recognition**: Supports both 12-hour and 24-hour formats.

## Security Features

1. **Input Size Limit**: Rejects files larger than 10KB to prevent Denial of Service (DoS) attacks.
2. **XSS Protection**: Detects and sanitizes `<script>` tags in the input to avoid potential cross-site scripting vulnerabilities in downstream systems.
3. **Data Masking**: Automatically masks the usernames of email addresses (e.g., `user@domain.com` becomes `u***@domain.com`) to protect user privacy in logs and outputs.

## How to Run

Ensure you have Python 3 installed.

1.  Place your raw text in `sample_input.txt`.
2.  Run the extractor:
    ```bash
    python3 REGEX.py
    ```
3.  The results will be printed in a clean JSON format.

## Example Output

```json
{
    "emails": ["s***@tech-solutions.co.uk"],
    "phone_numbers": ["(555) 123-4567"],
    "currency_amounts": ["$1,250.50"],
    "times": ["14:30"]
}
```

## Repository Structure
- `REGEX.py`: Core logic and regex patterns.
- `sample_input.txt`: Realistic test data.
- `README.md`: Project overview and usage.