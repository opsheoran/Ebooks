file_path = 'Sampling/Chapter2.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('<section id="sec2-3"')
end = content.find('<section id="sec2-4"')
sec23_content = content[start:end]

parts = sec23_content.split('<div class="hinglish-content">')
if len(parts) > 1:
    hinglish_content = parts[-1]
    print('Hinglish content for 2.3 length:', len(hinglish_content))
    print('Preview of Hinglish 2.3:', hinglish_content[:500])
else:
    print('Hinglish content not found in Section 2.3')
