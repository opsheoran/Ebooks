import os
import re
from bs4 import BeautifulSoup

def clean_html(html_str):
    # Remove "Hello students, welcome to the BSc First Year Statistics course."
    html_str = re.sub(r'Hello students,\s*welcome to the BSc First Year\s*Statistics\s*course\.', '', html_str, flags=re.IGNORECASE)
    # Remove any stray "Hello students,"
    html_str = re.sub(r'Hello students,', '', html_str, flags=re.IGNORECASE)
    
    # Fix the div.head -> h2 or h3
    soup = BeautifulSoup(html_str, 'html.parser')
    for head in soup.find_all('div', class_='head'):
        num = head.find('div', class_='num')
        title = head.find('h2', class_='title') or head.find('h3', class_='title') or head.find('h4', class_='title')
        
        if num and title:
            num_text = num.get_text(strip=True)
            title_text = title.get_text(strip=True)
            
            # Determine level based on numbering (e.g. 1.1 -> h2, 1.1.1 -> h3)
            dots = num_text.count('.')
            tag_name = 'h2' if dots == 1 else ('h3' if dots == 2 else 'h4')
            
            new_tag = soup.new_tag(tag_name)
            new_tag.string = f"{num_text} {title_text}"
            head.replace_with(new_tag)
            
    # For any remaining h2/h3 without proper formatting, just keep them.
    # Convert div.section to div.topic-section for our tab navigation.
    # Actually, we can just return the inner HTML of the sections.
    return str(soup)

def get_sections():
    with open('Stat-101/Chapter1.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    sections_html = ""
    # Find all sections except exercises
    for section in soup.find_all('div', class_='section'):
        if 'exercises' in section.get('id', '').lower():
            continue
        
        # Get inner HTML of section
        # The section has a div.head inside usually. We wrap each section in a section-card
        sec_content = "".join([str(child) for child in section.children])
        cleaned_content = clean_html(sec_content)
        
        sections_html += f"""
        <div class="topic-section active" id="{section.get('id', 'sec')}">
            <section class="section-card">
                <div class="english-content">
                    {cleaned_content}
                </div>
                <div class="hinglish-content" style="display:none;">
                    {cleaned_content}
                </div>
            </section>
        </div>
        """
    return sections_html

with open('extracted_theory.html', 'w', encoding='utf-8') as f:
    f.write(get_sections())

print("Extracted theory to extracted_theory.html")
