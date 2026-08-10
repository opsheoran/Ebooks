import re

file_path = 'Sampling/Chapter7.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Count single $ before replacement
single_dollars = re.findall(r'(?<!\$)\$(?!\$)', content)
print(f"Found {len(single_dollars)} single $ signs before replacement.")

# We want to replace matching pairs of single $ with \( and \)
# We can do this safely using a regex that captures the content between the $ signs
# provided there are no newlines inside the inline math (or there are, but we use re.DOTALL cautiously).
# Usually inline math doesn't span multiple paragraphs.
# Pattern: single $, followed by anything that is not a single $, followed by single $.
new_content = re.sub(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', r'\(\1\)', content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replacement done.")
