import bs4
soup = bs4.BeautifulSoup(open('Stat-101/Unit-II.html', encoding='utf-8'), 'html.parser')
for t in soup.find_all('div', class_='topic-section'):
    if t.get('id') == 'properties':
        print(t.prettify()[:1000])
