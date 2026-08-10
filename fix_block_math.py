import re

with open('Sampling/Chapter7.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace block math $$ ... $$ with \( ... \)
# We use a non-greedy match to find pairs of $$
new_content = re.sub(r'\$\$(.*?)\$\$', r'\(\1\)', content, flags=re.DOTALL)

with open('Sampling/Chapter7.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replaced all $$ with \(")