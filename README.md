# Secure Data Extraction Tool

This is a simple, interactive program that finds important information in text. It can extract URLs, Emails, Phone Numbers, Credit Cards, Time, and Rwandan Currency (Rwf).

## How to use

1.  **Run the program**:
    ```bash
    python3 REGEX.py
    ```
2.  **Choose what you want to extract**: Type a number from 1 to 7.
3.  **Choose the input**: Type 'yes' to use the built-in sample or 'no' to type your own text.
4.  **See the results**: The found items will appear in a simple list.

## Features

- **Specific Data**: Finds names like **Ngabonziza**, **Rugwiro**, and **Nshuti** in emails.
- **Local Currency**: Specifically looks for Rwandan Francs (**Rwf**).
- **Web Links**: Finds links like `apple.com` and `igihe.com`.
- **Safety First**: Automatically blocks dangerous scripts and keeps your data safe.
- **Privacy**: Partially hides email addresses (like `n***@example.rw`) to protect identity.

## Example Output

If you choose to extract **Emails** using the sample text, you will see:
- n***@example.rw
- r***@company.com
- n***@dev.org

If you choose **Currency**, you will see:
- Rwf 1,500,000
- Rwf 500,000

## How it works
The tool uses **Regular Expressions (Regex)** to find patterns in the text. It also checks the size of the text and looks for malicious code before it starts searching to make sure your system stays secure.