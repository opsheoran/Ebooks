import re

def check_balance(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    sections = re.finditer(r'<section(.*?)>(.*?)</section>', text, flags=re.DOTALL)
    for i, s in enumerate(sections):
        sec_text = s.group(0)
        div_open = sec_text.count('<div')
        div_close = sec_text.count('</div')
        if div_open != div_close:
            print(f"Mismatch in section {i}: {s.group(1).strip()}")
            print(f"  <div: {div_open}, </div: {div_close}")

check_balance('Sampling/Chapter3.html')
