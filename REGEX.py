import re

# Sample text with the names, URLs, and currency you requested
sample_text = """
Hello,
Please visit https://www.apple.com, https://www.igihe.com or https://mail.google.com for more info.
You can contact our team: ngabonziza@example.rw, rugwiro.work@company.com, or nshuti.official@dev.org.
Our support lines are (250) 788-123456 and 078-123-4567.
For payments, use credit card 1234-5678-9012-3456.
The total cost is Rwf 1,500,000. We already paid Rwf 500,000 at 10:30 AM.
The next meeting is at 14:30 or 4:00 PM.
"""

class DataExtractor:
    def __init__(self, text):
        self.text = text

    def validate_input(self, text):
        # Stop if text is too large (over 10,000 characters)
        if len(text) > 10000:
            print("Error: The text is too large. Please keep it under 10,000 characters.")
            return None
        
        # Check for dangerous script tags and hide them
        if re.search(r'<script.*?>', text, re.IGNORECASE):
            print("Security Alert: Found a script tag. It will be hidden for safety.")
            text = re.sub(r'<script.*?>.*?</script>', '[REDACTED]', text, flags=re.IGNORECASE | re.DOTALL)
        
        return text

    def extract_urls(self):
        # Finds web links starting with http or https
        pattern = r'https?://[a-zA-Z0-9.-]+(?:/[^\s,()\]]*)?'
        return list(set(re.findall(pattern, self.text)))

    def extract_emails(self):
        # Finds email addresses and hides the username for privacy
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        found = re.findall(pattern, self.text)
        masked = []
        for email in found:
            user, domain = email.split('@')
            masked.append(user[0] + "***@" + domain if len(user) > 1 else "***@" + domain)
        return list(set(masked))

    def extract_phone_numbers(self):
        # Finds phone numbers in various formats
        pattern = r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4,6}'
        return list(set(re.findall(pattern, self.text)))

    def extract_credit_cards(self):
        # Finds credit card numbers (16 digits with dashes or spaces)
        pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
        return list(set(re.findall(pattern, self.text)))

    def extract_time(self):
        # Finds time in 12-hour or 24-hour formats
        pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
        return list(set(re.findall(pattern, self.text)))

    def extract_currency(self):
        # Finds Rwandan currency (Rwf followed by numbers)
        pattern = r'Rwf\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
        return list(set(re.findall(pattern, self.text)))

if __name__ == "__main__":
    print("Welcome to the Data Extractor Tool")

    while True:
        print("\nWhat would you like to extract?")
        print("1. URLs")
        print("2. Emails")
        print("3. Phone Numbers")
        print("4. Credit Card Numbers")
        print("5. Time Formats")
        print("6. Currency (Rwf)")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        # Map choices to labels and functions
        menu = {
            "1": ("URLs", "extract_urls"),
            "2": ("Emails", "extract_emails"),
            "3": ("Phone Numbers", "extract_phone_numbers"),
            "4": ("Credit Card Numbers", "extract_credit_cards"),
            "5": ("Times", "extract_time"),
            "6": ("Currency amounts", "extract_currency")
        }

        if choice in menu:
            label, func_name = menu[choice]
            print(f"\nYou chose to extract: {label}")
            
            use_sample = input("Do you want to use the sample text? (yes/no): ").strip().lower()

            if use_sample == "yes":
                text = sample_text
            else:
                text = input("\nEnter the text you want to search:\n")

            extractor = DataExtractor(text)
            
            # Security check
            safe_text = extractor.validate_input(text)
            if safe_text is None:
                continue
            
            # Re-update extractor text with safe version
            extractor.text = safe_text
            
            # Get the results from the chosen function
            extract_func = getattr(extractor, func_name)
            results = extract_func()

            print(f"\n{label} Found:")
            if results:
                for item in results:
                    print(f"  - {item}")
            else:
                print("  No items found.")
        else:
            print("Invalid choice. Please pick a number between 1 and 7.")
