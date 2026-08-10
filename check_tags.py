file_path = 'Sampling/Chapter7.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print('Number of <div class="derivation-block">:', content.count('<div class="derivation-block">'))
print('Number of </div>:', content.count('</div>'))
print('Number of <div class="english-content">:', content.count('<div class="english-content">'))
print('Number of <div class="hinglish-content">:', content.count('<div class="hinglish-content">'))

# Let's also find all \( ... \)
import re
inline_math = re.findall(r'\\\(.*?\\\)', content, flags=re.DOTALL)
print(f'Number of \( ... \) equations: {len(inline_math)}')
