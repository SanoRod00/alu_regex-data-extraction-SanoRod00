# Secure Data Extraction Tool

This is a simple, interactive program that finds important information in text. It can extract URLs, Emails, Phone Numbers, Credit Cards, Time, and Rwandan Currency (Rwf).

## How to use

1.  Run the program:
    ```bash
    python3 REGEX.py
    ```
2.  Choose what you want to extract by typing a number (1-7).
3.  Decide if you want to use the **built-in sample text** or type in your **own text**.
4.  The results will be shown clearly on the screen.

## Features

- **Built-in Sample**: No need to prepare a file; just type 'yes' when asked.
- **Privacy**: Email addresses are partially hidden to protect people's identity.
- **Safety Checks**: The tool automatically blocks dangerous scripts and prevents handling of texts that are too large.

## Extracted Data
- **URLs**: Web links starting with http or https.
- **Emails**: Addresses (e.g., ngabonziza, rugwiro, nshuti).
- **Phones**: Contacts in various formats.
- **Credit Cards**: 16-digit payment numbers.
- **Time**: 12-hour (PM/AM) and 24-hour formats.
- **Currency**: Rwandan Francs (Rwf).