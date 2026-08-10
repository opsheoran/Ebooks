import glob, re

for f in glob.glob('Sampling/*.html'):
    with open(f, encoding='utf-8') as file:
        text = file.read()
    
    # We ignore the literal JS string '${topicId}' which has $
    text = text.replace('${topicId}', '')
    
    # Find single $
    single_dollars = re.findall(r'(?<!\$)\$(?!\$)', text)
    if len(single_dollars) > 0:
        print(f"{f} has {len(single_dollars)} single dollars")
        
        # print some context for the first one
        match = re.search(r'(?<!\$)\$(?!\$)', text)
        if match:
            start = max(0, match.start() - 30)
            end = min(len(text), match.end() + 30)
            print(f"   Context: {text[start:end]}")
