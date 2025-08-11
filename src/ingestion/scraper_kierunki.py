import requests
from bs4 import BeautifulSoup
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://ue.poznan.pl/kandydaci/kierunki-studiow/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(URL, headers=headers, verify=False)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'html.parser')

sections = soup.find_all('div', class_='accordionTabs tabbedDetailsFiltered__tab')

categories = [
    "Studia I stopnia stacjonarne",
    "Studia I stopnia niestacjonarne",
    "Studia II stopnia stacjonarne",
    "Studia II stopnia niestacjonarne",
    "Studia II stopnia (rekrutacja na semestr letni)"
]
counts = [14, 9, 19, 9, 3]

result = {}

section_index = 0
for cat_name, count in zip(categories, counts):
    kierunki_dict = {}
    for _ in range(count):
        section = sections[section_index]
        section_index += 1

        tab_value = section.get('data-tabbed-details-filtered-tab', '')
        parts = tab_value.split('-studia-')
        if len(parts) > 1:
            kierunek = parts[0].replace('-', ' ').title()
        else:
            kierunek = tab_value.replace('-', ' ').title()

        kierunek_data = {}

        text_sections = section.select('div.accordionTabs__sections > div.accordionTabs__section')
        tab_buttons = section.select('ul.sideCategories li.sideCategories__item span.sideCategories__linkTitle')

        for i, text_section in enumerate(text_sections):
            try:
                tab_name = tab_buttons[i].get_text(strip=True).lower()
            except IndexError:
                tab_name = f"sekcja_{i+1}"

            content_div = text_section.select_one('div.accordionTabs__text.wysiwyg')
            if content_div:
                ps = content_div.find_all(['p', 'ul', 'ol', 'div'], recursive=False)
                texts = []
                for el in ps:
                    text = el.get_text(strip=True, separator=' ')
                    if len(texts)==0 and kierunek.lower() in text.lower() and len(text)<50:
                        continue
                    texts.append(text)
                section_text = "\n".join(texts).strip()
                section_text = section_text.replace('\n', ' ')

            else:
                section_text = text_section.get_text(strip=True, separator=' ')

            if "opis" in tab_name:
                key = "opis kierunku"
            elif "rekrutacja" in tab_name:
                key = "rekrutacja"
            elif "specjalno" in tab_name:
                key = "specjalności"
            elif "program" in tab_name:
                key = "program studiów"
            else:
                key = tab_name

            kierunek_data[key] = section_text

        kierunki_dict[kierunek] = kierunek_data

    result[cat_name] = kierunki_dict

# ścieżka
output_path = r""
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
