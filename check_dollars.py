import re

file_path = 'Sampling/Chapter7.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

single_dollars = re.findall(r'(?<!\$)\$(?!\$)', content)
print(f"Remaining single $ signs: {len(single_dollars)}")

# Check if there are any remaining
if len(single_dollars) > 0:
    # Print the context around the remaining single $
    for match in re.finditer(r'(?<!\$)\$(?!\$)', content):
        start = max(0, match.start() - 30)
        end = min(len(content), match.end() + 30)
        print(f"Context: ...{content[start:end]}...")
