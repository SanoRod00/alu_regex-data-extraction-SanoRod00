# Secure Data Extraction Tool

This program finds important information like Emails, URLs, Phone Numbers, Currency (Rwf), and Time from your text files. It is built to be simple and safe.

## Features

- **Email Extraction**: Finds emails and hides part of them for privacy.
- **URL Extraction**: Finds links like `https://www.apple.com`.
- **Phone Numbers**: Finds local and international phone formats.
- **Currency**: Specifically looks for Rwandan Francs (e.g., `Rwf 500`).
- **Time**: Finds time in both 12-hour and 24-hour styles.

## Security

1. **Size Limit**: It ignores files that are too large (above 10KB) to keep things fast.
2. **Script Blocking**: It automatically removes dangerous `<script>` tags from the input.
3. **Privacy**: It masks the start of emails (like `n***@example.rw`) so personal data stays safe.

## How to use

1.  Put your text in the `sample_input.txt` file.
2.  Run the script:
    ```bash
    python3 REGEX.py
    ```
3.  You will see the results in a clear list.

## Example Output

```json
{
    "emails": ["n***@example.rw"],
    "urls": ["https://www.apple.com"],
    "currency_amounts": ["Rwf 1,500,000"],
    "times": ["10:30 AM"]
}
```