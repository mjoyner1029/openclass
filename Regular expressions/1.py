import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
exclude_domain = "exclude.com"

# Construct the regex pattern to exclude email addresses from 'exclude.com'
pattern = r"\b[A-Za-z0-9._%+-]+@(?!{})(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b".format(re.escape(exclude_domain))

# Find all email addresses except those from 'exclude.com'
emails = re.findall(pattern, text)

print(emails)