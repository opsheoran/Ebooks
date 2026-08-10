with open('Sampling/Chapter3.html', 'r', encoding='utf-8') as f:
    text = f.read()

s9 = text.find('<section id="sec3-9"')
s10 = text.find('<section id="sec3-10"')
s11 = text.find('<section id="sec3-11"')

print("Section 3.9 HTML:")
print(text[s9:s10])

print("\n--- Section 3.10 HTML:")
print(text[s10:s11])
