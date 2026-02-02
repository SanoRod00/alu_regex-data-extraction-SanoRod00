import re
import json

class DataExtractor:
    """
    A secure data extraction tool that uses regex to identify structured data from raw text.
    Handles Emails, URLs, Phone Numbers, Currency, and Time.
    """

    def __init__(self):
        # Email: Matches standard emails, including subdomains and plus-tags
        # Security: Simple structure to avoid catastrophic backtracking
        self.email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        # URL: Matches http/https protocols with domain and optional path/query
        self.url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*\??[\w\.-]*=?[\w\.-]*'

        # Phone: Matches (123) 456-7890, 123-456-7890, 123.456.7890
        self.phone_pattern = r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}'

        # Currency: Matches $19.99, $1,234.56
        self.currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

        # Time: Matches 14:30, 2:30 PM, 11:59 AM (12 and 24 hour)
        self.time_pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APMapm]{2})?\b'

    def validate_input(self, text):
        """
        Security check to prevent DoS or processing of obviously malicious scripts.
        """
        # 1. Length check (DoS protection)
        if len(text) > 10000:
            raise ValueError("Input text too large. Maximum allowed is 10,000 characters.")

        # 2. Basic XSS/Injection detection (Ignore patterns that look like script tags)
        if re.search(r'<script.*?>', text, re.IGNORECASE):
            # We don't throw an error, we just strip or warn. For this tool, we'll log it.
            print("[SECURITY WARNING] Potential script injection detected in input.")
            # Sanitize: Remove script tags
            text = re.sub(r'<script.*?>.*?</script>', '[REDACTED SCRIPT]', text, flags=re.IGNORECASE | re.DOTALL)
        
        return text

    def mask_email(self, email):
        """
        Masks email addresses to protect sensitive data.
        Example: user@example.com -> u***@example.com
        """
        user, domain = email.split('@')
        if len(user) > 1:
            return user[0] + "***@" + domain
        return "***@" + domain

    def extract_all(self, text):
        """
        Processes text and extracts all supported data types.
        Returns a structured dictionary with findings.
        """
        # Validate and sanitize
        try:
            clean_text = self.validate_input(text)
        except ValueError as e:
            return {"error": str(e)}

        results = {
            "emails": [self.mask_email(e) for e in re.findall(self.email_pattern, clean_text)],
            "urls": re.findall(self.url_pattern, clean_text),
            "phone_numbers": re.findall(self.phone_pattern, clean_text),
            "currency_amounts": re.findall(self.currency_pattern, clean_text),
            "times": re.findall(self.time_pattern, clean_text)
        }

        # Deduplicate results
        for key in results:
            if isinstance(results[key], list):
                results[key] = list(set(results[key]))

        return results

if __name__ == "__main__":
    import os

    extractor = DataExtractor()
    input_file = "sample_input.txt"

    if os.path.exists(input_file):
        with open(input_file, "r") as f:
            raw_data = f.read()
        
        extracted_data = extractor.extract_all(raw_data)
        
        print("\n--- DATA EXTRACTION RESULTS ---")
        print(json.dumps(extracted_data, indent=4))
        print("-------------------------------\n")
    else:
        print(f"Error: {input_file} not found. Please create it first.")
