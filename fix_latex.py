import re

with open('Sampling/Chapter7.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace paired $ with \( and \)
# Ensure we don't match $$ which are already used for block math.
text = re.sub(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', r'\(\1\)', text)

with open('Sampling/Chapter7.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Regex replacement completed.")