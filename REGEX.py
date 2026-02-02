import re
import json

class DataExtractor:
    """
    This class finds emails, URLs, phone numbers, currency, and time in text.
    It also keeps the data safe from malicious input.
    """

    def __init__(self):
        # Finds standard email addresses
        self.email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        # Finds web links starting with http or https
        self.url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*\??[\w\.-]*=?[\w\.-]*'

        # Finds phone numbers in different formats
        self.phone_pattern = r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4,6}'

        # Finds Rwandan currency (e.g., Rwf 500 or Rwf 1,000)
        self.currency_pattern = r'Rwf\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

        # Finds time in 12-hour or 24-hour formats
        self.time_pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APMapm]{2})?\b'

    def validate_input(self, text):
        """
        Checks if the input is too long or has dangerous scripts.
        """
        # Stop if the text is too big (over 10,000 letters)
        if len(text) > 10000:
            raise ValueError("The text is too long! Please keep it under 10,000 characters.")

        # Look for dangerous <script> tags and remove them
        if re.search(r'<script.*?>', text, re.IGNORECASE):
            print("[SAFE CHECK] Found a script tag. Redacting it for safety.")
            text = re.sub(r'<script.*?>.*?</script>', '[REDACTED]', text, flags=re.IGNORECASE | re.DOTALL)
        
        return text

    def mask_email(self, email):
        """
        Hides part of the email for privacy.
        """
        user, domain = email.split('@')
        if len(user) > 1:
            return user[0] + "***@" + domain
        return "***@" + domain

    def extract_all(self, text):
        """
        Runs the extraction and returns the found items in a clean list.
        """
        try:
            clean_text = self.validate_input(text)
        except ValueError as e:
            return {"error": str(e)}

        # Find all matches for each type
        results = {
            "emails": [self.mask_email(e) for e in re.findall(self.email_pattern, clean_text)],
            "urls": re.findall(self.url_pattern, clean_text),
            "phone_numbers": re.findall(self.phone_pattern, clean_text),
            "currency_amounts": re.findall(self.currency_pattern, clean_text),
            "times": re.findall(self.time_pattern, clean_text)
        }

        # Remove duplicates
        for key in results:
            if isinstance(results[key], list):
                results[key] = list(set(results[key]))

        return results

if __name__ == "__main__":
    import os

    extractor = DataExtractor()
    filename = "sample_input.txt"

    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = f.read()
        
        found = extractor.extract_all(data)
        
        print("\n--- RESULTS ---")
        print(json.dumps(found, indent=4))
        print("---------------\n")
    else:
        print(f"File {filename} not found.")
