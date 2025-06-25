# Get Domain Name Information using Python

import whois

# Prompt user for domain input
domain = input("Enter your domain (e.g., example.com): ")

# Fetch domain information
domain_info = whois.whois(domain)

# Display domain info
for key, value in domain_info.items():
    print(f"{key}: {value}")
