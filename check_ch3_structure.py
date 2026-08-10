with open('Sampling/Chapter3.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Number of <div class="hinglish-content">:', text.count('<div class="hinglish-content">'))
print('Number of <div class="english-content">:', text.count('<div class="english-content">'))
print('Number of <section:', text.count('<section'))
print('Number of </section>:', text.count('</section>'))
