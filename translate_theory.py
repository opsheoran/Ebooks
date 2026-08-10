import urllib.request, urllib.parse, json, re, time
from bs4 import BeautifulSoup, NavigableString

def translate_text(text):
    if not text.strip() or not re.search('[a-zA-Z]', text):
        return text
    try:
        q = urllib.parse.quote(text.strip())
        url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=hi&dt=t&q={q}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        translated = "".join([chunk[0] for chunk in data[0] if chunk[0]])
        
        # Restore leading/trailing spaces
        prefix = ' ' if text.startswith(' ') or text.startswith('\n') else ''
        suffix = ' ' if text.endswith(' ') or text.endswith('\n') else ''
        return prefix + translated + suffix
    except Exception as e:
        print("Error translating:", text[:30], e)
        time.sleep(1) # Backoff on error
        return text

def process_file(in_file, out_file):
    with open(in_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # We only want to translate the contents inside div.english-content and put them into div.hinglish-content
    for section in soup.find_all('div', class_='topic-section'):
        eng_div = section.find('div', class_='english-content')
        hin_div = section.find('div', class_='hinglish-content')
        
        if eng_div and hin_div:
            # We copy the english div content to a new soup
            hin_soup = BeautifulSoup(str(eng_div), 'html.parser')
            # Translate all text nodes in hin_soup
            nodes = hin_soup.find_all(string=True)
            total = len(nodes)
            for i, node in enumerate(nodes):
                if isinstance(node, NavigableString):
                    trans = translate_text(str(node))
                    node.replace_with(trans)
                if i % 20 == 0:
                    print(f"Translating node {i}/{total} in section {section.get('id')}")
            
            # Replace hin_div content with translated children
            hin_div.clear()
            for child in hin_soup.div.children:
                hin_div.append(child)
                
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print("Starting translation...")
process_file('extracted_theory.html', 'extracted_theory_translated.html')
print("Done!")
