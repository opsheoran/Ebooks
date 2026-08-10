import re
content = open('Sampling/Chapter7.html', encoding='utf-8').read()
matches = re.findall(r'<div class="derivation-block">(.*?)</div>', content, flags=re.DOTALL)
for i, m in enumerate(matches[:3]):
    print(f'Block {i}: {repr(m)}')
