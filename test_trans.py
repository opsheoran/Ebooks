import urllib.request, urllib.parse, json, re
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
        
        # Restore leading/trailing spaces if any
        prefix = ' ' if text.startswith(' ') or text.startswith('\n') else ''
        suffix = ' ' if text.endswith(' ') or text.endswith('\n') else ''
        return prefix + translated + suffix
    except Exception as e:
        print("Error translating:", text[:30], e)
        return text

html = "<p>Hello <strong>world</strong>! How are you?</p>"
soup = BeautifulSoup(html, "html.parser")
for node in soup.find_all(string=True):
    if isinstance(node, NavigableString):
        node.replace_with(translate_text(str(node)))
print(str(soup))
